from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginForm, name="registration.login"),
    path('signup/',views.signForm, name="registration.signup"),
    path('store/',views.registrationStore,name="registration.store"),
]