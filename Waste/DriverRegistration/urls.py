from django.urls import path
from . import views


urlpatterns = [
    path('driverlogin/',views.loginForm, name="driver.login"),
    path('driversignup/',views.SignupPage, name="driver.signup"),

    path('list/', views.vehicleList, name='driver.list'),
    path('store', views.vehicleStore,name='driver.store'),
    path('add', views.vehicleCreate,name='driver.create'),
    path('edit/<int:id>', views.vehicleEdit,name='driver.edit'),
    path('delete/<int:id>', views.vehicleDelete,name='driver.delete'),
    path('update/<int:id>', views.vehicleUpdate,name='driver.update'),
    
]