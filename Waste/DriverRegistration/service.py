from .models import RegisterVehicle


def storeVehicle(request):
    vehicle=RegisterVehicle(
        user_id =request.user.id,
        vehicle_no=request.POST['vehicle_no'],
        vehicle_type=request.POST['vehicle_type'],
        driver_name=request.POST['driver_name'],
        driver_license_no=request.POST['driver_license_no'],
        driver_photo  =request.FILES.get('driver_photo',False),
        license_photo =request.FILES.get('license_photo',False),
        created_at=request.POST.get('created_at',False),
        updated_at=request.POST.get('updated_at',False),
        
    )
    vehicle.save()
    return "sucess"


def updateVehicle(request,id):
    vehicle=RegisterVehicle.objects.get(id=id)
    vehicle.vehicle_no = request.POST["vehicle_no"]
    vehicle.vehicle_type=request.POST["vehicle_type"]
    vehicle.driver_name= request.POST['driver_name']
    vehicle.driver_license_no=request.POST['driver_license_no']
    vehicle.driver_photo=request.FILES.get('driver_photo',False)
    vehicle.license_photo=request.FILES.get('license_photo',False)
    vehicle.created_at=request.POST.get('created_at',False)
    vehicle.updated_at=request.POST.get('updated_at',False)
    vehicle.save()
    return "sucess"

def deleteVehicle(id):
    vehicle = RegisterVehicle.objects.get(id = id)
    vehicle.delete()
    return "success"

def getVehicleId(id):
    vehicle = RegisterVehicle.objects.get(id= id)
    return vehicle

def getVehicle():
    vehicle =  RegisterVehicle.objects.values().all()
    return list(vehicle)