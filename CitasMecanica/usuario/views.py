from django.shortcuts import redirect, render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import UserCreationForm, AuthenticationForm, profileform, userupdate, mecanicoform
from django.contrib import auth
from django.contrib import messages
from.models import Profile
from mecanico.models import Mecanico
from django.contrib.auth.models import User, Group
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

    return render(request, 'autenticacion/SignIn.html', data)

def registrar(request):
    data = {
        'form': UserCreationForm()
    }
    
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Clientes')
            user.groups.add(group)
            user = auth.authenticate(username = form.cleaned_data["username"], password =form.cleaned_data["password1"])
            auth.login(request, user)
            messages.success(request, "Te has registrado con exito")
            return redirect(to="home") 
        data["form"] = form
    return render(request, "autenticacion/SignUp.html", data)

def profileupdate(request):
    usuario= get_object_or_404(User, pk=request.user.id)
    perfil= []
    data = {}
    if usuario.groups.filter(name='Clientes').exists():
        perfil = get_object_or_404(Profile, user=usuario.id)
        data = {
            "userform":userupdate(instance=usuario),
            'profile': profileform(instance=perfil),
            'role': 'Cliente'
        }
        if request.method == 'POST':
            formulario2 = userupdate(data=request.POST,instance=usuario)
            formulario = profileform(data=request.POST, instance=perfil)
            if formulario.is_valid() and formulario2.is_valid():
                formulario.save()
                formulario2.save()
                messages.success(request, f'El Perfil se modificó con exito')
                return redirect(to="profileUser")
            else:
                data["profile"] = formulario
                data["userform"]= formulario2
    else:
        perfil = get_object_or_404(Mecanico, user=usuario.id)
        data = {
            "userform":userupdate(instance=usuario),
            'profile': mecanicoform(instance=perfil),
            'role': 'Mecánico'
        }
        if request.method == 'POST':
            formulario2 = userupdate(request.POST,instance=usuario)
            formulario = []
            if usuario.groups.filter(name='Clientes').exists():
                formulario = profileform(data=request.POST, instance=perfil)
            else:
                formulario = mecanicoform(request.POST, request.FILES, instance=perfil)
            if formulario.is_valid() and formulario2.is_valid():
                print('Si')
                formulario.save()
                formulario2.save()
                return redirect(to="profileUser")
            else:
                print('Error')
                data["profile"] = formulario
                data["userform"]= formulario2
    return render(request, 'usuario/ProfileUpdate.html', data)

def renderprofile(request):
    usuario= get_object_or_404(User, pk=request.user.id)
    perfil= []
    role = []
    if usuario.groups.filter(name='Clientes').exists():
        perfil = get_object_or_404(Profile, user=usuario.id)
        role = "Cliente"
    else:
        perfil = get_object_or_404(Mecanico, user=usuario.id)
        role = "Mecánico"
    data={'profile':perfil,'user':usuario, 'role': role}
    return render(request,'usuario/Profile.html',data)

