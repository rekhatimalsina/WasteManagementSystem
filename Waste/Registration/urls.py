from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginForm, name="registration.login"),
    path('',views.firstpage, name="first"),
    path('signup/',views.SignUpForm, name="registration.signup"),
    #path('store/',views.registrationStore,name="registration.store"),
]