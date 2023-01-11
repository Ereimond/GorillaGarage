from django.shortcuts import redirect, render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import UserCreationForm, AuthenticationForm,profileform,userupdate,vehiculoforms,vehiculoupdateform
from django.contrib import auth
from django.contrib import messages
from.models import profile, vehiculo
from django.contrib.auth.models import User
# Create your views here.

def autent(request):
    data = {
        'form': AuthenticationForm()
    }
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username = form.cleaned_data["username"], password =form.cleaned_data["password"])
            auth.login(request, user)
            return redirect(to="home") 
        data["form"] = form

    return render(request, 'usuario/autent.html', data)

def registrar(request):
    data = {
        'form': UserCreationForm()
    }
    
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username = form.cleaned_data["username"], password =form.cleaned_data["password1"])
            auth.login(request, user)
            messages.success(request, "Te has registrado con exito")
            return redirect(to="home") 
        data["form"] = form
    return render(request, "usuario/registro.html", data)

def profileupdate(request, id):
    perfil = get_object_or_404(profile, user = id)
    user=get_object_or_404(User,pk=perfil.user.id)
    data = {
        "userform":userupdate(instance=user),
        'profile': profileform(instance=perfil)
        
    }
    if request.method == 'POST':
        formulario2 = userupdate(data=request.POST,instance=user)
        formulario = profileform(data=request.POST, instance=perfil)
        if formulario.is_valid() and formulario2.is_valid():
            formulario.save()
            formulario2.save()
            messages.success(request, f'El Perfil se modificó con exito')
            return redirect(to="home")
        else:
            data["profile"] = formulario
            data["userform"]= formulario2
    return render(request, 'usuario/profileupdate.html', data)

def renderprofile(request,id):
    perfil= get_object_or_404(profile, pk=id)
    usuario= get_object_or_404(User, pk=id)
    data={'profile':perfil,'user':usuario}
    return render(request,'usuario/profile.html',data)

def rendervehiculo(request):
    vehiculos=vehiculo.objects.filter(duenio=request.user.id)
    print(request.user)
    data={
        "vehiculos":vehiculos,
    }
    return render(request, "vehiculo/vehiculo.html",data)

def vehiculoupdate(request,id):
    vehiculos= get_object_or_404(vehiculo, pk=id)
    
    data = {
        'editvehiculo' : vehiculoupdateform(instance=vehiculos)
    }

    if request.method == 'POST':
        formulario = vehiculoupdateform(data=request.POST, instance=vehiculos)
        if formulario.is_valid():
            formulario.save()
            
            return redirect(to="vehiculo")
        data["editvehiculo"] = formulario

    return render(request, "vehiculo/vehiculo.html", data)


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
            print('fallo')
            data["vehiculoadd"]=formulario
    return render(request, "vehiculo/vehiculoadd.html",data)

def deletevehiculo(request,id):
    vehiculos=get_object_or_404(vehiculo,id=id)
    vehiculos.delete()
    return redirect(to="vehiculo")