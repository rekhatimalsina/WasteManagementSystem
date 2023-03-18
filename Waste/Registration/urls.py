from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginForm, name="registration.login"),
   
]