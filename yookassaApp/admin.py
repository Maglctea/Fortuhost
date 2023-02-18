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

@admin.register(Transaction)
class AppAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'value', 'currency', 'created_at', 'updated_at', 'transaction_token')
    list_filter = ('status', 'currency')
    ordering = ('user', 'pk', 'status', 'currency', 'created_at', 'updated_at')
    list_per_page = 20
    search_fields = ('user__username', 'transaction_token')
    list_display_links = ('user', 'status')


admin.site.register(TransactionStatus)
admin.site.register(Currensy)
admin.site.register(Refund)
admin.site.register(RefundStatus)
