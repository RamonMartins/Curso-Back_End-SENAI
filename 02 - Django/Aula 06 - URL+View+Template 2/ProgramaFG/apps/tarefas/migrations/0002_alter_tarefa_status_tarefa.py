# Generated by Django 4.2.5 on 2023-09-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='status_tarefa',
            field=models.BooleanField(default=False, verbose_name='Concluído'),
        ),
    ]
