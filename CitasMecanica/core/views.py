from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    usuario= get_object_or_404(User, pk=request.user.id)
    role = []
    if usuario.groups.filter(name='Clientes').exists():
        role = "Cliente"
    else:
        role = "Mecánico"
    data={'role': role}
    return render(request, 'core/home.html', data)