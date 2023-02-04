from django.db import models
from mecanico.models import Mecanico
from vehiculo.models import Vehiculo
from usuario.models import Profile

# Create your models here.
class Citas(models.Model):
    cliente = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo', null=True, blank=True)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE, verbose_name='Mecánico', null=True, blank=True)
    descripcion = models.CharField(max_length=550, verbose_name="Descripción", null=True, blank=True)
    ingreso = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de ingreso")
    entrega = models.DateField(verbose_name="Fecha de Salida", null=True, blank=True)

    
    def __str__(self):
        return f"{self.cliente.user.first_name} {self.vehiculo.marca}"

    class Meta:
        verbose_name = 'cita'
        verbose_name_plural = 'citas'