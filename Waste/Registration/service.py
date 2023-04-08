from .models import Customer


def storeCustomer(request):
    customer=Customer(
        user_id =request.user.id,
        name=request.POST['name'],
        address=request.POST['address'],
        mobile=request.POST['mobile'],
        photo  =request.FILES.get('customer_photo ',False),
        created_at=request.POST.get('created_at',False),
        updated_at=request.POST.get('updated_at',False),    
    )
    customer.save()
    return "sucess"

def updateCustomer(request,id):
    customer=Customer.objects.get(id=id)
    customer.name = request.POST["name"]
    customer.address=request.POST["address"]
    customer.mobile= request.POST['mobile']
    customer.photo=request.FILES.get('photo',False)
    customer.created_at=request.POST.get('created_at',False)
    customer.updated_at=request.POST.get('updated_at',False)
    customer.save()
    return "sucess"

def deleteCustomer(id):
    customer = Customer.objects.get(id = id)
    customer.delete()
    return "success"

def getCustomerId(id):
    customer = Customer.objects.get(id= id)
    return customer

def getCustomer():
    customer =  Customer.objects.values().all()
    return list(customer)