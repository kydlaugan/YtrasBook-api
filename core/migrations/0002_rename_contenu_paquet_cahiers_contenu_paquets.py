# Generated by Django 4.2.4 on 2023-09-12 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cahiers',
            old_name='contenu_paquet',
            new_name='contenu_paquets',
        ),
    ]
