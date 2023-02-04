from django.urls import path

from support.views import BugReport

urlpatterns = [
    path('', BugReport.as_view(), name='support')
]