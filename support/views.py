from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView, CreateView

from djangoProject.settings import EMAIL_HOST_USER
from support.forms import BugReportForm
from django.core.mail import send_mail


class BugReport(CreateView):
    form_class = BugReportForm
    template_name = 'mail/bug_report.html'

    def form_valid(self, form):
        form.save()
        send_mail('Обработка багрепорта', 'Отчет принят в обработку. Спасибо за обращение', f'Fortuhost <{EMAIL_HOST_USER}>', [self.request.user.email])
        return redirect('dashboard')

    # support = send_mail(form.changed_data['subject'], form.changed_data['content'], EMAIL_HOST_USER, [self.request.user.email], fail_silently=True)

    #     app = App.objects.create(user=self.request.user, title=form.data['title'], description=form.data['description'])
    #
    #     path = f'app/docker_task/{app.pk}'
    #     os.mkdir(path)
    #
    #     fs = FileSystemStorage(location=path)
    #     fs.save(f'{app.pk}.zip', form.files['file'])
    #
    #     # create_container.delay(app.pk)
    #     create_container.s(app.pk).apply_async()
    #     return redirect('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Создание обращения'
        return context