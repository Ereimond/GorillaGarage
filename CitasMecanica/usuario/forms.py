from tkinter.ttk import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from.models import profile, vehiculo
class UserCreationForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )
    first_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "first_name",
                'placeholder' : "Primer Nombre"
            }
        )
    )
    last_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "last_name",
                'placeholder' : "Apellido"
            }
        )
    )
    email=forms.EmailField(
         widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "email",
                'id' : "email",
                'placeholder' : "Correo Electronico"
            }
        )
    )
    password1=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password1",
                'placeholder' : "Contraseña"
            }
        )
    )
    password2=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password2",
                'placeholder' : "Verificar Contraseña"
            }
        )
    )
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password",
                'placeholder' : "Contraseña"
            }
        )
    )
class profileform(forms.ModelForm):
    ocupacion=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "ocupacion",
                'placeholder' : " "
            }
        )
    )
    telefono=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "telefono",
                'placeholder' : ""
            }
        )
    )
    direccion=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "direccion",
                'placeholder' : " "
            }
        )
    )
    fechanacimiento=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "date",
                'id' : "fechanacimiento",
                'placeholder' : " "
            }
        )
    )


    class Meta:
        model=profile 
        exclude=['user']
        fields=['direccion','ocupacion','fechanacimiento','telefono']

class userupdate(forms.ModelForm):
    first_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "first_name",
                'placeholder' : "Primer Nombre"
            }
        )
    )
    last_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "last_name",
                'placeholder' : "Apellido"
            }
        )
    )
    class Meta:
        model=User
        fields=['first_name','last_name']

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
        model=vehiculo
        fields=['duenio','placa','marca','modelo','anovehiculo']

class vehiculoupdateform(forms.ModelForm):
    placa=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "placaedit",
                'placeholder' : " "
            }
        )
    )
    marca=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "marcaedit",
                'placeholder' : " "
            }
        )
    )
    modelo=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "modeloedit",
                'placeholder' : " "
            }
        )
    )

    anovehiculo=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "date",
                'id' : "anovehiculoedit",
                'placeholder' : " "
            }
        )
    )
    class Meta:
        model=vehiculo
        fields=['placa','marca','modelo','anovehiculo']
