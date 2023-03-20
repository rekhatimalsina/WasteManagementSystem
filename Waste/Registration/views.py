from django.shortcuts import render,HttpResponse,redirect

from Registration.models import Registration

# Create your views here.
def loginForm(request):
    data={
        'title':'Member Registration'
    }
    return render(request,"registration/login.html",data)

def signForm(request):
    data={
        'title':'signup'
    }
    return render(request,"registration/signup.html",data)
def registrationStore(request):
    if request.method=='POST':
        password=request.POST['password']
        confirm_password=request.POST['cpassword']

        if password!= confirm_password:
            return HttpResponse("Your password and confrim password doesnot match")
        
        else:
            registration=Registration(
              email= request.POST['email'],
              full_name= request.POST['full_name'],
              dob= request.POST['dob'],
              password= request.POST['password'],
              confirm_password= request.POST['cpassword'],
              created_at= request.POST.get('created_at',False),
              updated_at= request.POST.get('updated_at',False)
              
              )
            registration.save()
            return redirect('registration.login')
        return render(request,'registration/signup.html')

              



            
