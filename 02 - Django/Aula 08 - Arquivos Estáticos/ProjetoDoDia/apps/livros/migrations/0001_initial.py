# Generated by Django 4.2.5 on 2023-09-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_livro', models.CharField(max_length=200)),
                ('descricao_livro', models.TextField()),
            ],
        ),
    ]
