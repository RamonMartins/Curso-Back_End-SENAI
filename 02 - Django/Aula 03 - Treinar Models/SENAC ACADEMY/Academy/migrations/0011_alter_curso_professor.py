# Generated by Django 4.2.4 on 2023-08-23 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0010_alter_curso_carga_horaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Academy.professor'),
            preserve_default=False,
        ),
    ]
