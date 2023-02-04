from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    direccion=models.CharField(max_length=150,blank=True,null=True,verbose_name="direccion")
    telefono=models.CharField(max_length=10,blank=True,null=True,verbose_name="telefono")
    ocupacion=models.CharField(max_length=30,blank=True,null=True,verbose_name="ocupacion")
    fechanacimiento=models.DateField(blank=True,null=True,verbose_name="fecha de nacimiento")
    def __str__(self):
        return f"{self.user.username} | {self.user.first_name}"

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'