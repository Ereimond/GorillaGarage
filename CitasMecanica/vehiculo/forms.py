from django import forms
from .models import Vehiculo

class vehiculoforms(forms.ModelForm):
    placa=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "placa",
                'placeholder' : " "
            }
        )
    )
    marca=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "marca",
                'placeholder' : " "
            }
        )
    )
    modelo=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "modelo",
                'placeholder' : " "
            }
        )
    )

    anovehiculo=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "date",
                'id' : "anovehiculo",
                'placeholder' : " "
            }
        )
    )
    
    class Meta:
        model=Vehiculo
        fields=['duenio','placa','marca','modelo','anovehiculo']

class vehiculoupdateform(forms.ModelForm):
    placa=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "placaedit",
                'placeholder' : ""
            }
        )
    )
    marca=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "marcaedit",
                'placeholder' : ""
            }
        )
    )
    modelo=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "modeloedit",
                'placeholder' : ""
            }
        )
    )

    anovehiculo=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "date",
                'id' : "anovehiculoedit",
                'placeholder' : ""
            }
        )
    )
    class Meta:
        model=Vehiculo
        fields=['placa','marca','modelo','anovehiculo']