# Generated by Django 4.1.5 on 2023-01-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0005_rename_user_id_contacto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='link',
            field=models.URLField(),
        ),
    ]