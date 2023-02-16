from django.contrib import admin
from yookassaApp.models import TransactionStatus, Transaction, Currensy, Refund, RefundStatus

# @admin.register(models.User)
# class CustomUserAdmin(UserAdmin):
#
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (_("Personal info"), {"fields": ("first_name", "last_name", "email", "wallet",)}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#
#     form = UserChangeForm
#     add_form = UserCreationForm
#     change_password_form = AdminPasswordChangeForm
#     list_display = ("username", "email", "first_name", "last_name", "is_staff")
#     list_filter = ("is_staff", "is_superuser", "is_active", "groups")
#     search_fields = ("username", "first_name", "last_name", "email")
#     ordering = ("username",)
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )


admin.site.register(TransactionStatus)
admin.site.register(Currensy)
admin.site.register(Transaction)
admin.site.register(Refund)
admin.site.register(RefundStatus)
