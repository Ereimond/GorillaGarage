# Generated by Django 4.0 on 2023-02-02 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=150, null=True, verbose_name='direccion')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='telefono')),
                ('ocupacion', models.CharField(blank=True, max_length=30, null=True, verbose_name='ocupacion')),
                ('fechanacimiento', models.DateField(blank=True, null=True, verbose_name='fecha de nacimiento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
            },
        ),
    ]
