from django.contrib import admin
from django.urls import path
from app.views import dashboard, app, edit_app, test, logoutUser, RegisterUser, LoginUser, main
from app.forms import *

urlpatterns = [
    path('', main, name='main'),
    path('apps/', dashboard, name='dashboard'),
    path('apps/<int:pk>/', app, name='apps'),
    path('app/<int:pk>/', edit_app, name='app'),
    # path('signup/', register_user, name='register'),
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('signin/', LoginUser.as_view(), name='signin'),
    path('logout/', logoutUser, name='logout')

    # path('test/<int:pk>', test, name='test'),

]