# Generated by Django 4.2.4 on 2023-08-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('valor_produto', models.DecimalField(decimal_places=2, max_digits=1000)),
            ],
        ),
    ]
