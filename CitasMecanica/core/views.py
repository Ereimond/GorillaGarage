from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuario.models import servicio

# Create your views here.
@login_required
def home(request):
    servics = servicio.objects.all()
    data = {
        'servicios': servics
    }
    return render(request, "core/home.html", data)