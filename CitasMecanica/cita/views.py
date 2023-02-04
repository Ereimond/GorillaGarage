from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from cita.models import Citas
from .forms import CitasForm
from mecanico.models import Mecanico
from usuario.models import Profile
from vehiculo.models import Vehiculo

# Create your views here.
def renderCita(request):
    usuario= get_object_or_404(User, pk=request.user.id)
    role = []
    citas = []
    if usuario.groups.filter(name='Clientes').exists():
        perfil = get_object_or_404(Profile, user=usuario.id)
        citas=Citas.objects.filter(cliente=request.user.id)
        role = "Cliente"
    else:
        perfil = get_object_or_404(Mecanico, pk = usuario.id)
        citas=Citas.objects.filter(mecanico=request.user.id)
        role = "Mecánico"
    
    data={
        "citas":citas,
        'role':role
    }
    return render(request, "cita/cita.html",data)

def citaAdd(request):
    usuario = get_object_or_404(User, pk = request.user.id)
    perfil = get_object_or_404(Profile, user=usuario.id)
    vehiculos = Vehiculo.objects.filter(duenio=perfil.id)
    mecanicos = Mecanico.objects.all()
    data = { 'form': CitasForm(), 'usuario': usuario, 'mecanicos':mecanicos,
        'profile': perfil,
        'vehiculos': vehiculos }
    if request.method == 'POST':
        formulario = CitasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            print(request.POST)
            return redirect(to="cita")
        else:
            data["form"] = formulario
    return render(request, "cita/citaAdd.html", data)

def citaUpdate(request, id):
    usuario = get_object_or_404(User, pk = request.user.id)
    perfil = get_object_or_404(Profile, user=usuario.id)
    citas = get_object_or_404(Citas, pk=id)
    vehiculo = get_object_or_404(Vehiculo, pk = citas.vehiculo.id)
    vehiculos = Vehiculo.objects.filter(duenio=perfil.id)
    mecanico = get_object_or_404(Mecanico, pk = citas.mecanico.id)
    mecanicos = Mecanico.objects.all()
    data = { 'form': CitasForm(instance=citas), 'usuario': usuario, 'mecanicos':mecanicos, 'mecanico':mecanico,
        'profile': perfil,
        'vehiculos': vehiculos,
         'vehiculo':vehiculo }

    if request.method == 'POST':
        formulario = CitasForm(data=request.POST, instance=citas)
        if formulario.is_valid():
            formulario.save()
            print(request.POST)
            return redirect(to="cita")
        data["form"] = formulario
    return render(request, 'cita/citaUpdate.html', data)

def citaDelete(request,id):
    cita=get_object_or_404(Citas,pk=id)
    cita.delete()
    return redirect(to="cita")