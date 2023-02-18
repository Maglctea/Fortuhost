from django.contrib import admin
from app.models import App, AppStatus

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'title', 'docker_id', 'app_status', 'time_create', 'time_update', 'time_start'
    )
    list_filter = ('app_status',)
    ordering = ('user', 'pk',)
    list_per_page = 10
    search_fields = ('user__username', 'title')
    list_display_links = ('user', 'title')


@admin.register(AppStatus)
class AppAdmin(admin.ModelAdmin):
    list_display = ('status', 'color', 'permission_start', 'permission_stop', 'permission_restart', 'permission_delete')
    ordering = ('pk',)
    list_display_links = ('status', 'color')

