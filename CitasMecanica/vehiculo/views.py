from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo
from .forms import vehiculoforms, vehiculoupdateform
from django.contrib.auth.models import User

# Create your views here.
def rendervehiculo(request):
    usuario= get_object_or_404(User, pk=request.user.id)
    role = []
    if usuario.groups.filter(name='Clientes').exists():
        role = "Cliente"
    else:
        role = "Mecánico"
    vehiculos=Vehiculo.objects.filter(duenio=request.user.id)
    vehiculoUpdate = vehiculoupdateform()
    
    data={
        "vehiculos":vehiculos,
        "vehiculoUpdate": vehiculoUpdate,
        'role':role
    }
    return render(request, "vehiculo/vehiculo.html",data)

def vehiculoupdate(request):
    product = Vehiculo.objects.get(pk=request.POST.get("idVehiculo"))
    formulario = vehiculoupdateform(
        request.POST, instance=product
    )
    if formulario.is_valid:
        formulario.save()
        return redirect(to="vehiculo")


def vehiculoadd(request):
    data={
        'vehiculoadd':vehiculoforms()
    }
    if request.method=='POST':
        formulario=vehiculoforms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='vehiculo')
        else: 
            data["vehiculoadd"]=formulario
    return render(request, "vehiculo/vehiculoAdd.html",data)

def deletevehiculo(request,id):
    vehiculos=get_object_or_404(Vehiculo,id=id)
    vehiculos.delete()
    return redirect(to="vehiculo")