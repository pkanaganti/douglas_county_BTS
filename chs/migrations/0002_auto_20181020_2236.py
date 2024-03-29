# Generated by Django 2.0 on 2018-10-21 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='CoordinatorID',
            new_name='NumberofPatients',
        ),
        migrations.AddField(
            model_name='event',
            name='CoordinatorName',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='InjuryLevel',
            field=models.CharField(choices=[('good/fair', 'Good/Fair'), ('serious', 'Serious'), ('critical', 'Critical'), ('expired', 'Expired')], default='good/fair', max_length=10),
        ),
    ]
