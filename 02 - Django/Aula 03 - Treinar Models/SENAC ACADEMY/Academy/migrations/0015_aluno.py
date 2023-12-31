# Generated by Django 4.2.4 on 2023-08-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0014_delete_alunos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Aluno')),
                ('idade', models.IntegerField()),
                ('data_de_nascimento', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('sobre_mim', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
