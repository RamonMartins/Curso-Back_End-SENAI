# Generated by Django 4.2.4 on 2023-08-23 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0015_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadoPessoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=10)),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Academy.aluno')),
            ],
        ),
    ]
