from django.contrib import admin
from django.urls import path
from yookassaApp.views import CreateTransaction, webhook_transaction
from app.forms import *

urlpatterns = [
    path('webhook/', webhook_transaction, name='webhook'),
    path('transaction/create/', CreateTransaction.as_view(), name='create_transaction')
    # path('test/<int:pk>', test, name='test'),

]