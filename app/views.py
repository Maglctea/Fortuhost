import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from app.forms import AppEditForm, CustomUserCreationForm, CustomUserChangeForm, CustomUserAuthenticationForm, \
    AppCreateForm
from app.models import App, AppStatus
from django.http import Http404
from app.tasks import *


@login_required
def dashboard(request):
    context = {'apps': App.objects.filter(user_id=request.user.pk).order_by('-pk'),
               'page_name': 'Приложения'}
    return render(request, 'app/apps.html', context)


@login_required
def app(request, pk):
    app = App.objects.get(pk=pk)

    if request.method == 'POST':
        form = AppEditForm(request.POST, instance=app)
        if form.is_valid():
            form.save()

    context = {'form': AppEditForm(instance=app),
               'app': app,
               'page_name': 'Приложение'}

    return render(request, 'app/app.html', context)



@login_required
def app_start(request, pk):
    app = App.objects.get(pk=pk, user=request.user)
    app.app_status = AppStatus.objects.get(pk=2)
    app.save()
    start_container.s(pk).apply_async()
    return redirect('dashboard')


@login_required
def app_stop(request, pk):
    app = App.objects.get(pk=pk, user=request.user)
    app.app_status = AppStatus.objects.get(pk=1)
    app.save()
    stop_container.s(pk).apply_async()
    return redirect('dashboard')


@login_required
def app_restart(request, pk):
    app = App.objects.get(pk=pk, user=request.user)
    app.app_status = AppStatus.objects.get(pk=3)
    app.save()
    restart_container.s(pk).apply_async()
    return redirect('dashboard')


@login_required
def app_delete(request, pk):
    App.objects.get(pk=pk, user=request.user).delete()
    delete_container.s(pk).apply_async()
    return redirect('dashboard')


@login_required
def app_status(request):
    apps_list = App.objects.filter(user_id=request.user.pk)
    apps = {}
    for app in apps_list:
        app_status = app.app_status
        status = {
            'id_status': app_status.pk,
            # 'name_status': app_status.status,
            'color': app_status.color,
            'permission_start': app.app_status.permission_start,
            'permission_stop': app.app_status.permission_stop,
            'permission_restart': app.app_status.permission_restart,
            'permission_delete': app.app_status.permission_delete

        }
        apps[app.pk] = {'status': status}
    return JsonResponse(apps)


@login_required
def edit_app(request, pk):
    app = App.objects.get(pk=pk)
    return HttpResponse(AppEditForm(instance=app).as_p())


def test(request, pk):
    app = App.objects.get(pk=pk)
    context = {'form': AppEditForm(instance=app),
               'app': app}
    return render(request, 'app/test.html', context)

@login_required
def logoutUser(request):
    logout(request)
    res = redirect('signin')
    return res


def main(request):
    context = {'page_name': 'Главная'}
    return render(request, 'app/main.html', context)


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'app/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')


class LoginUser(LoginView):
    form_class = CustomUserAuthenticationForm
    template_name = 'app/signin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Вход'
        return context


class CreateApp(FormView):
    form_class = AppCreateForm
    template_name = 'app/add_app.html'

    def form_valid(self, form):
        app = App.objects.create(user=self.request.user, title=form.data['title'], description=form.data['description'])

        path = f'app/docker_task/{app.pk}'
        os.mkdir(path)

        fs = FileSystemStorage(location=path)
        fs.save(f'{app.pk}.zip', form.files['file'])

        # create_container.delay(app.pk)
        create_container.s(app.pk).apply_async()
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Создание приложения'
        return context


class EditApp(LoginRequiredMixin, UpdateView):
    login_url = '/signin/'
    redirect_field_name = 'signin'
    form_class = AppEditForm
    template_name = 'app/edit_app.html'
    model = App

    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Изменение приложения'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk is None:
            return redirect('signin')
        get_object_or_404(App, pk=kwargs['pk'], user=request.user)
        return super(EditApp, self).dispatch(request, *args, **kwargs)


