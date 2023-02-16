import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from yookassa import Refund, Receipt, Payment
from yookassa.domain.common import ConfirmationType, SecurityHelper
from yookassa.domain.models import ReceiptItem, Currency
from yookassa.domain.notification import WebhookNotificationFactory, WebhookNotificationEventType
from yookassa.domain.request import PaymentRequestBuilder

from accounts.models import CustomUser
from yookassaApp.forms import TransationCreateForm
from yookassaApp.models import Transaction, TransactionStatus, RefundStatus
import yookassaApp.models
import uuid


# Create your views here.
def start_pay():
    idempotence_key = str(uuid.uuid4())
    refund = Refund.create({
        "amount": {
            "value": "2.00",
            "currency": "RUB"
        },
        "payment_id": "215d8da0-000f-50be-b000-0003308c89be"
    }, idempotence_key)

    print(refund)


class CreateTransaction(LoginRequiredMixin, CreateView):
    form_class = TransationCreateForm
    template_name = 'yookassaApp/payment.html'

    def form_valid(self, form):
        transaction = Transaction.objects.create(user=self.request.user, value=form.cleaned_data['value'])
        ip = get_client_ip(self.request)

        builder = PaymentRequestBuilder()
        builder.set_amount({"value": transaction.value, "currency": Currency.RUB}) \
            .set_confirmation({"type": ConfirmationType.REDIRECT, "return_url": "https://fortuhost.ru"}) \
            .set_capture(False) \
            .set_description("Пополнение баланса") \
            .set_metadata({"token": str(transaction.transaction_token),
                           "client_id": self.request.user.pk, })
        request = builder.build()

        res = Payment.create(request)
        transaction.transaction_token = res.id
        transaction.save()

        # payment = json.loads((Payment.find_one(payment_id)).json())
        return redirect(res.confirmation.confirmation_url)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def edit_transaction(token, paymentStatus):
    Transaction.objects.filter(transaction_token=token).update(status=TransactionStatus.objects.get(name=paymentStatus))

@csrf_exempt
def webhook_transaction(request):
    # Проверка, что запрос пришел от ЮКассы:
    ip = get_client_ip(request)  # Получите IP запроса
    if not SecurityHelper().is_ip_trusted(ip):
        return HttpResponse(status=400)

    # Извлечение JSON объекта из тела запроса
    response_object = json.loads(request.body)
    try:
        # Создание объекта класса уведомлений в зависимости от события
        if response_object['status'] == 'succeeded':
            transaction = Transaction.objects.get(transaction_token=response_object['id'])
            user = transaction.user
            user.wallet += transaction.value
            user.save()
            transaction.status = TransactionStatus.objects.get(name=response_object['status'])
            transaction.save()
        elif response_object['status'] == 'waiting_for_capture':
            edit_transaction(response_object['id'], response_object['status'])
        elif response_object['status'] == 'canceled':
            edit_transaction(response_object['id'], response_object.status)
        else:
            # Обработка ошибок
            return HttpResponse(status=400)  # Сообщаем кассе об ошибке
    except Exception:
        # Обработка ошибок
        return HttpResponse(status=400)  # Сообщаем кассе об ошибке

    return HttpResponse(status=200)  # Сообщаем кассе, что все хорошо