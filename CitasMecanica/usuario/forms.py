from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile
from mecanico.models import Mecanico

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
                'placeholder' : "Ocupación"
            }
        )
    )
    telefono=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "telefono",
                'placeholder' : "Teléfono"
            }
        )
    )
    direccion=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "direccion",
                'placeholder' : "Dirección"
            }
        )
    )
    fechanacimiento=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "date",
                'id' : "fechanacimiento",
                'placeholder' : "Fecha de Nacimiento"
            }
        )
    )


    class Meta:
        model=Profile 
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

class mecanicoform(forms.ModelForm):
    cargo=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "cargo",
                'placeholder' : "Cargo"
            }
        )
    )
    telefono=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "telefono",
                'placeholder' : "Teléfono"
            }
        )
    )
    direccion=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "direccion",
                'placeholder' : "Dirección"
            }
        )
    )
    fechanacimiento=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "date",
                'id' : "fechanacimiento",
                'placeholder' : "Fecha de Nacimiento"
            }
        )
    )

    imagen = forms.ImageField(
        widget=forms.FileInput(
        attrs={
                'class': 'form-control',
                'type':'file',
                'id' : "imagen",
                'placeholder' : "Foto de Perfil"
        })
    )
    class Meta:
        model=Mecanico 
        exclude=['user']
        fields=['imagen','direccion','cargo','fechanacimiento','telefono']