# Generated by Django 2.0.5 on 2018-11-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chs', '0015_auto_20181126_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Condition_on_arrival',
            field=models.CharField(choices=[('good/fair', 'Good/Fair'), ('serious', 'Serious'), ('critical', 'Critical'), ('expired', 'Expired')], max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Department',
            field=models.CharField(choices=[('ICU/CC', 'ICU/CC'), ('ER', 'ER'), ('Med/Surg', 'Med/Surg'), ('OB', 'OB'), ('SICU', 'SICU'), ('Neg_Pres_Iso', 'Neg Pres/Iso'), ('OR', 'OR'), ('Peds', 'Peds'), ('PICU', 'PICU'), ('NICU', 'NICU'), ('Burn', 'Burn'), ('Mental Health', 'Mental Health'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Disposition_type',
            field=models.CharField(choices=[('To home', 'To home'), ('Other Hospital', 'Other Hospital'), ('SNF', 'SNF'), ('ICF', 'ICF')], max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Injury_type',
            field=models.CharField(choices=[('Cuts', 'Cuts'), ('Strains/Sprains', 'Strains/Sprains'), ('Burns', 'Burns'), ('Abrasions', 'Abrasions'), ('Internal Injuries', 'Internal Injuries'), ('Fractures', 'Fractures'), ('Respiratory Conditions', 'Respiratory Conditions'), ('Others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Kin_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Relationship_To_Victim',
            field=models.CharField(choices=[('Wife', 'Wife'), ('Mother', 'Mother'), ('Father', 'Father'), ('Husband', 'Husband'), ('Daughter', 'Daughter'), ('Son', 'Son'), ('Others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Room_No_If_Admitted',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Triage_Tag_colour',
            field=models.CharField(choices=[('Green', 'Green'), ('Yellow', 'Yellow'), ('Red', 'Red'), ('Black', 'Black')], max_length=10),
        ),
    ]
