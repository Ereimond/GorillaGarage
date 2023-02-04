"""CitasMecanica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core
from usuario import views as usuario
from django.conf import settings
from vehiculo import views as vehiculo
from mecanico import views as mecanico
from cita import views as cita
from django.contrib.auth import views as auth_views #import this

urlpatterns = [
    path('', core.home, name="home"),
    path('admin/', admin.site.urls), 
    path('login/', usuario.autent, name='SignIn'),
    path('registro/', usuario.registrar, name='SignUp'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('perfil/modificar/',usuario.profileupdate,name='profileUpdate'),
    path('perfil/',usuario.renderprofile,name='profileUser'),
    path('restablecer-contraseña/', auth_views.PasswordResetView.as_view(template_name="autenticacion/password-reset.html"), name='password_reset'),
    path('restablecer-contraseña-enviado/', auth_views.PasswordResetDoneView.as_view(template_name="autenticacion/password_reset_done.html"), name='password_reset_done'),
    path('restablecer/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="autenticacion/password-confirm.html"), name='password_reset_confirm'),
    path('restablecer-contraseña-completa/', auth_views.PasswordResetCompleteView.as_view(template_name="autenticacion/password_reset_complete.html"), name='password_reset_complete'),

    #------------------------------------------------------------------------
    
    path('vehiculo/',vehiculo.rendervehiculo,name='vehiculo'),
    path('vehiculo/modificar/',vehiculo.vehiculoupdate,name='vehiculoupdate'),
    path('vehiculo/añadir/',vehiculo.vehiculoadd,name='vehiculoAdd'),
    path('vehiculo/eliminar/<id>/',vehiculo.deletevehiculo,name='deletevehiculo'),

    #------------------------------------------------------------------------
    
    path('mecanicos/',mecanico.mecanicos,name='mecanicos'),

    #------------------------------------------------------------------------
    
    path('citas/',cita.renderCita,name='cita'),
    path('citas/añadir',cita.citaAdd,name='citaAdd'),
    path('citas/modificar/<id>/',cita.citaUpdate,name='citaUpdate'),
    path('citas/eliminar/<id>/',cita.citaDelete,name='vehiculoDelete'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)