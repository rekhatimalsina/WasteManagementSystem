from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginForm, name="registration.login"),
    path('',views.firstpage, name="first"),
    path('signup/',views.SignUpForm, name="registration.signup"),
    path('logout/',views.LogoutPage, name='registration.logout'),
    #path('profile/',views.customerProfiles, name='registration.profiles'),

    path('list/', views.customerList, name='customer.list'),
    path('store', views.customerStore,name='customer.store'),

    path('add', views.customerCreate,name='customer.create'),
    path('edit/<int:id>', views.customerEdit,name='customer.edit'),
    path('delete/<int:id>', views.customerDelete,name='customer.delete'),
    path('update/<int:id>', views.customerUpdate,name='customer.update'),
    path('store/',views.customerProfiles,name="customer.profile"),
    path('home1/',views.home,name="home"),
    path('profiles/',views.one_user,name="profiles")
    
]
  
