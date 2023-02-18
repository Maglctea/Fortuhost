from django.contrib import admin
from accounts.models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'wallet',
        'date_joined', 'last_login', 'is_active', 'is_superuser'
    )
    list_filter = ('is_active', 'is_superuser')
    ordering = ('last_login', 'is_active',)
    list_per_page = 20
    search_fields = ('first_name', 'last_name', 'username', 'email')
    actions = ('mark_as_delete', 'mark_as_active', 'mark_as_superuser', 'mark_as_user')
    list_display_links = ('email', 'username')
