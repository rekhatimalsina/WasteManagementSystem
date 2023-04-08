from django.shortcuts import render,HttpResponse,redirect
#from django.views.generic import View, TemplateView,
# from Registration.models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View, TemplateView
from .models import Customer

from . import service

def firstpage(request):
    return render(request,"registration/index.html")

def SignUpForm(request):
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
        return redirect('registration.login')

    return render (request,'registration/signup.html')



def loginForm(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render (request,'registration/home.html')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'registration/login.html')



#driver ko lagi banako template chai mapping garxa
def customerCreate(request):
    data={
        'title':"customer"
    }
    return render(request,'registration/addUser.html',data)



#template bata leko data database gayera save gariraxa
def customerStore(request):
   # print(request.POST)
    store= service.storeCustomer(request)
    return redirect('customer.list')



#database ko data template ma show gariraxa
def customerList(request):
    #customer=Customer.objects.all()
    customer=Customer.objects.values().filter(user_id=request.user.id)
    data={
        'customer':customer,

    }
    return render(request,'registration/list.html',data)


#edit form redirect garxa.
def customerEdit(request,id):
    customer=service.getCustomerId(id)
    data={
        'title':'customer',
        # 'driver':service.getVehicleId(id),
        'customer':customer
    }
    return render(request,'/addDriver.html',data)

#update the data in database template 
def customerUpdate(request,id):
    service.updateCustomer(request, id)
    return redirect('home')


#delete a data from a database
def customerDelete(request,id):
    service.deleteCustomer(id)
    return redirect('customer.list')

def LogoutPage(request):
    logout(request)
    return redirect('registration.login')


def customerProfiles(request, id=None):
    customer = Customer.objects.get(user=id)
    context = {
        'customer': customer
    }
    return render(request, 'registration/viewCustomer.html', context)
def home(request):
    return render(request,'registration/home.html')



def one_user(request, id=None):
    customer = Customer.objects.get(id=1)
    context = {
        'customer': customer
    }
    return render(request, 'registration/profiles.html', context)