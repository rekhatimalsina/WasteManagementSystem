from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User

from DriverRegistration import service
from .models import RegisterVehicle




# this login form is for login driver.
def loginForm(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('driver.list')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'Driver/login.html')

#this signup page for driver signup
def SignupPage(request):
    if request.method=='POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')

        if password1 != password2:
            #messages.success(request, 'first password and second password is not correct!!!')
            return HttpResponse("Your password and confrom password doesnot match !!!")
        if User.objects.filter(username=username).first():
            #messages.success(request, "Such a user has already registered!!!")
            return HttpResponse('Such a user has already registered!!!')

        if User.objects.filter(email=email).first():
            #messages.success(request, "This email has already been registered!!!")
            return HttpResponse('This email has already been registered!!!')
        user_obj = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
        user_obj.set_password(raw_password=password1)
        user_obj.save()
        return redirect('driver.login')

    return render (request,'Driver/signup.html')

#driver ko lagi banako template chai mapping garxa
def vehicleCreate(request):
    data={
        'title':"driver"
    }
    return render(request,'Driver/addDriver.html',data)

#template bata leko data database gayera save gariraxa
def vehicleStore(request):
   # print(request.POST)
    store= service.storeVehicle(request)
    return redirect('driver.list')

#database ko data template ma show gariraxa
def vehicleList(request):
    #driver=RegisterVehicle.objects.all()
    driver=RegisterVehicle.objects.values().filter(user_id=request.user.id)
    data={
        'driver':driver,

    }
    return render(request,'driver/list.html',data)


#edit form redirect garxa.
def vehicleEdit(request,id):
    driver=service.getVehicleId(id)
    data={
        'title':'product',
        # 'driver':service.getVehicleId(id),
        'driver':driver
    }
    return render(request,'Driver/addDriver.html',data)

#update the data in database template 
def vehicleUpdate(request,id):
    service.updateVehicle(request, id)
    return redirect('driver.list')
#delete a data from a database
def vehicleDelete(request,id):
    service.deleteVehicle(id)
    return redirect('driver.list')