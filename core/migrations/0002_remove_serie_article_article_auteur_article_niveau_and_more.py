# Generated by Django 4.2.4 on 2023-08-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='auteur',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='niveau',
            field=models.CharField(blank=True, choices=[('SIL', 'SIL'), ('CP', 'CP'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CM1', 'CM1'), ('CM2', 'CM2'), ('Class 1', 'Class 1'), ('Class 2', 'Class 2'), ('Class 3', 'Class 3'), ('Class 4', 'Class 4'), ('Class 5', 'Class 5'), ('Class 6', 'Class 6'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('Tle', 'Tle')], max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='serie',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('D', 'D'), ('E', 'E'), ('Ti', 'Ti'), ('Chinois', 'Chinois'), ('All/Esp', 'All/Esp')], max_length=2000),
        ),
        migrations.AlterField(
            model_name='article',
            name='matiere',
            field=models.CharField(choices=[('Langue Française', 'Langue Française'), ('Litterature', 'Litterature'), ('Anglais', 'Anglais'), ('Histoire', 'Histoire'), ('Geographie', 'Geographie'), ('Education à la citoyenneté', 'Education à la citoyenneté'), ('Langue et culture nationale', 'Langue et culture nationale'), ('Art', 'Art'), ('Mathematiques', 'Mathematiques'), ('Sciences', 'Sciences'), ('Informatique', 'Informatique'), ('Latin', 'Latin'), ('Langues Etrangère', 'Langues Etrangère'), ('SVT', 'SVT'), ('PCT', 'PCT'), ('Philosophie', 'Philosophie'), ('Physique', 'Physique'), ('Chimie', 'Chimie'), ('Arts cinematographiques', 'Arts cinematographiques'), ('Sciences Tles Litteraires', 'Sciences Tles Litteraires')], max_length=2000),
        ),
        migrations.DeleteModel(
            name='Niveau',
        ),
        migrations.DeleteModel(
            name='Serie',
        ),
    ]