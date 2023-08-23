# Generated by Django 4.2.4 on 2023-08-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_alter_livro_ano_lancamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='status',
            field=models.CharField(choices=[('0', 'PUBLISHED'), ('1', 'DRAFT'), ('2', 'FINISHED'), ('3', 'EXPIRED')], default=0, max_length=1),
        ),
    ]
