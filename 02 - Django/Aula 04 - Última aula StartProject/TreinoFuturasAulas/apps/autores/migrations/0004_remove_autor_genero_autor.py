# Generated by Django 4.2.4 on 2023-08-25 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0003_alter_autor_genero_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='genero_autor',
        ),
    ]
