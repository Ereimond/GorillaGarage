from django import forms
from .models import Citas
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    

    class Meta:
        model = User
        fields = ["first_name", "last_name"]



class CitasForm(forms.ModelForm):

    

    descripcion =forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "descripcion",
                "name":"descripcion",
                'placeholder' : "Agregue la causa"
            }
        )
    )

    entrega=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "date",
                'id' : "entrega",
                'placeholder' : ""
            }
        )
    )


    class Meta:
        model = Citas
        #fields ["name", "email", "type_consult", "message", "notice"]
        fields = '__all__'