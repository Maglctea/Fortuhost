# import os
#
# import var_dump as var_dump
# from yookassa import Refund, Configuration, Settings, Receipt, Payment
# import uuid
#
# from yookassa.domain.common import ConfirmationType
# from yookassa.domain.models import ReceiptItem, Currency
# from yookassa.domain.request import PaymentRequestBuilder
#
#
# def start_pay():
#     idempotence_key = str(uuid.uuid4())
#     refund = Refund.create({
#         "amount": {
#             "value": "2.00",
#             "currency": "RUB"
#         },
#         "payment_id": "215d8da0-000f-50be-b000-0003308c89be"
#     }, idempotence_key)
#
#     var_dump.var_dump(refund)
#
# def pay2():
#     receipt = Receipt()
#     receipt.customer = {"phone": "79990000000", "email": "test@email.com"}
#     receipt.tax_system_code = 1
#     receipt.items = [
#         ReceiptItem({
#             "description": "Product 1",
#             "quantity": 2.0,
#             "amount": {
#                 "value": 250.0,
#                 "currency": Currency.RUB
#             },
#             "vat_code": 2
#         })
#     ]
#
#     builder = PaymentRequestBuilder()
#     builder.set_amount({"value": 999, "currency": Currency.RUB}) \
#         .set_confirmation({"type": ConfirmationType.REDIRECT, "return_url": "https://merchant-site.ru/return_url"}) \
#         .set_capture(False) \
#         .set_description("Чайная революция") \
#         .set_metadata({"orderNumber": "72",
#                        "client_id": 777,}) \
#         # .set_receipt(receipt)
#
#     request = builder.build()
#     # Можно что-то поменять, если нужно
#     request.client_ip = '1.2.3.4'
#     res = Payment.create(request)
#
#     var_dump.var_dump(res)
#
# id_k = 853313
# key_k = 'live_vh2gETD-gmC258AyLMXHxaKj3UbLpGMmHKlZBeGczL0'
# conf = Configuration.configure(id_k, key_k)
# # me = Settings.get_account_settings()
# pay2()
# # receipt1()
# pass

# diapazon = int(input("Введите диапазон для поиска простых чисел: "))
# s = 1
# for num in range(1,diapazon):
#         count = 0
#         delitel = 2
#         while delitel<num:
#             if num%delitel == 0:
#                 count += 1
#             delitel += 1
#         if count == 0:
#             s *= num
#             print (f'{num} простое число')
# print(s)

# x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(x[2:-2:2])

10000 00111
11000 00011
11100 00001
11110 00000
01111 00000
00111 10000
00011 11000
00001 11100
00000 11110
00000 01111

