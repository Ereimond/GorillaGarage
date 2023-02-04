from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mecanico(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=f'mecanico/%Y/%m/%d', blank=True)
    direccion=models.CharField(max_length=150,blank=True,null=True,verbose_name="Dirección")
    telefono=models.CharField(max_length=10,blank=True,null=True,verbose_name="Teléfono")
    cargo=models.CharField(max_length=50,blank=True,null=True,verbose_name="Cargo")
    fechanacimiento=models.DateField(blank=True,null=True,verbose_name="Fecha de Nacimiento")
    def __str__(self):
        return f"{self.user.username} | {self.user.first_name}"

    class Meta:
        verbose_name = 'mecanico'
        verbose_name_plural = 'mecanicos'