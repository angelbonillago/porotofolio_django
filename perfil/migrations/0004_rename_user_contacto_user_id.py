# Generated by Django 4.1.5 on 2023-01-18 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_remove_proyectos_fecha_fin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='user',
            new_name='user_id',
        ),
    ]
