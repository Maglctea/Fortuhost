from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView, CreateView

from djangoProject.settings import EMAIL_HOST_USER
from support.forms import BugReportForm
from django.core.mail import send_mail


class BugReport(CreateView):
    form_class = BugReportForm
    template_name = 'support/bug_report.html'

    def form_valid(self, form):
        form.save()
        if not self.request.user.is_anonymous and self.request.user.email:
            msg = f'Отчет по теме «{form.data["subject"]}» принят в обработку. Спасибо за обращение'
            send_mail('Обработка обращение', msg, f'Fortuhost <{EMAIL_HOST_USER}>', [self.request.user.email])
            return redirect('dashboard')
        return redirect('main')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Создание обращения'
        return context
