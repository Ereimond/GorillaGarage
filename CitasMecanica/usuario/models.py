from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    direccion=models.CharField(max_length=150,blank=True,null=True,verbose_name="direccion")
    telefono=models.CharField(max_length=10,blank=True,null=True,verbose_name="telefono")
    ocupacion=models.CharField(max_length=30,blank=True,null=True,verbose_name="ocupacion")
    fechanacimiento=models.DateField(blank=True,null=True,verbose_name="fecha de nacimiento")
    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'


        
class vehiculo(models.Model):
    duenio = models.ForeignKey(profile, on_delete=models.CASCADE, blank=True, null=True)
    placa=models.CharField(max_length=30, blank=True, null=True,verbose_name="placa" )
    marca=models.CharField(max_length=30, blank=True, null=True,verbose_name="marca" )
    modelo=models.CharField(max_length=30, blank=True, null=True,verbose_name="modelo" )
    anovehiculo=models.DateField(blank=True, null=True,verbose_name="año del vehiculo" )
    
    def __str__(self):
        return f"{self.placa}"

    class Meta:
        verbose_name = 'vehiculo'
        verbose_name_plural = 'vehiculos'


class servicio(models.Model):
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50, blank=True, null=True, verbose_name="Titulo del Servicio")
    descripcion = models.CharField(max_length=200, blank=True, null=True, verbose_name="Descripcion del Servicio")
    precio = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Precio del Servcio")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'