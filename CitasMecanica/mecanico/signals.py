from .models import Mecanico
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_createProfile(sender, instance, created, *args, **kwargs):
    print(sender)
    print(instance)
    print(created)
    if created:
        Mecanico.objects.create(user=instance)