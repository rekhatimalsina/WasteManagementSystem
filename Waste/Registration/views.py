from django.shortcuts import render,HttpResponse,redirect

# from Registration.models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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



# # Create your views here.
# def loginForm(request):
#     data={
#         'title':'Member Registration'
#     }
#     return render(request,"registration/login.html",data)

# def signForm(request):
#     data={
#         'title':'signup'
#     }
#     return render(request,"registration/signup.html",data)
# def registrationStore(request):
#     if request.method=='POST':
#         password=request.POST['password']
#         confirm_password=request.POST['cpassword']

#         if password!= confirm_password:
#             return HttpResponse("Your password and confrim password doesnot match")
        
#         else:
#             registration=Registration(
#               email= request.POST['email'],
#               full_name= request.POST['full_name'],
#               dob= request.POST['dob'],
#               password= request.POST['password'],
#               confirm_password= request.POST['cpassword'],
#               created_at= request.POST.get('created_at',False),
#               updated_at= request.POST.get('updated_at',False)
              
#               )
#             registration.save()
#             return redirect('registration.login')
#         return render(request,'registration/signup.html')

              



            
