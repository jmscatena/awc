# Generated by Django 3.0 on 2025-05-28 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='creado_em',
            new_name='criado_em',
        ),
    ]
