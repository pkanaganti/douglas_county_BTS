# Generated by Django 2.0.5 on 2018-11-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chs', '0013_auto_20181112_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Time_of_Death',
        ),
        migrations.AddField(
            model_name='patient',
            name='Status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Injury_type',
            field=models.CharField(choices=[('Cuts', 'Cuts'), ('Strains/Sprains', 'Strains/Sprains'), ('Burns', 'Burns'), ('Abrasions', 'Abrasions'), ('Internal Injuries', 'Internal Injuries'), ('Fractures', 'Fractures'), ('Respiratory Conditions', 'Respiratory Conditions'), ('Others', 'Others')], default='', max_length=10),
        ),
    ]