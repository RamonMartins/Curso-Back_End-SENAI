# Generated by Django 4.2.4 on 2023-08-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0006_alter_alunos_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('carga_horaria', models.IntegerField()),
            ],
        ),
    ]