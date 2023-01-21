from django.contrib import admin
from django.urls import path
from app.views import *
from app.forms import *

urlpatterns = [
    path('', main, name='main'),
    path('apps/', dashboard, name='dashboard'),
    path('apps/<int:pk>/', app, name='apps'),
    path('apps/<int:pk>/start/', app_start, name='app_start'),
    path('apps/<int:pk>/stop/', app_stop, name='app_stop'),
    path('apps/<int:pk>/restart/', app_restart, name='app_restart'),
    path('apps/<int:pk>/delete/', app_delete, name='app_delete'),

    path('app/<int:pk>/', edit_app, name='app'),
    path('app/', CreateApp.as_view(), name='add_app'),
    # path('signup/', register_user, name='register'),
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('signin/', LoginUser.as_view(), name='signin'),
    path('logout/', logoutUser, name='logout'),
    path('appStatus/', app_status, name='appStatus')

    # path('test/<int:pk>', test, name='test'),

]