# Generated by Django 4.2.4 on 2023-08-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0003_alter_alunos_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]