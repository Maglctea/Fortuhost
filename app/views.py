from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from app.forms import AppEditForm, CustomUserCreationForm, CustomUserChangeForm, CustomUserAuthenticationForm
from app.models import App


@login_required
def dashboard(request):
    context = {'apps': App.objects.filter(user_id=request.user.pk),
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
def edit_app(request, pk):
    app = App.objects.get(pk=pk)
    return HttpResponse(AppEditForm(instance=app).as_p())


def test(request, pk):
    app = App.objects.get(pk=pk)
    context = {'form': AppEditForm(instance=app),
               'app': app}
    return render(request, 'app/test.html', context)


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
