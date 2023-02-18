from django.contrib import admin

from support.models import FeedbackType, Feedback


@admin.register(Feedback)
class AppAdmin(admin.ModelAdmin):
    list_display = ('subject', 'feedback_type', 'content', 'file')
    list_filter = ('feedback_type',)
    ordering = ('feedback_type', 'pk', 'subject')
    list_per_page = 10
    search_fields = ('subject', 'content')
    list_display_links = ('subject', 'feedback_type')


admin.site.register(FeedbackType)