# Generated by Django 2.0.5 on 2018-11-06 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chs', '0005_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='PatientDate_of_Birth',
            new_name='Date_of_Birth',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='PatientFirstName',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='PatientLastName',
            new_name='LastName',
        ),
        migrations.AddField(
            model_name='patient',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], default='Female', max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='Injury_type',
            field=models.CharField(choices=[('Cuts', 'Cuts'), ('Burns', 'Burns')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
