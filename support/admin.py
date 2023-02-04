from django.contrib import admin

from support.models import FeedbackType, Feedback

admin.site.register(FeedbackType)
admin.site.register(Feedback)