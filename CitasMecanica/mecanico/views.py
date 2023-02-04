from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Mecanico

# Create your views here.
def mecanicos(request):
    usuario= get_object_or_404(User, pk=request.user.id)
    role = []
    if usuario.groups.filter(name='Clientes').exists():
        role = "Cliente"
    else:
        role = "Mecánico"
    mecanico = Mecanico.objects.all()
    data={'role': role, 'mecanico':mecanico}
    return render(request, 'mecanico/mecanico.html', data)