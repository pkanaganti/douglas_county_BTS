# Generated by Django 2.0.5 on 2018-10-20 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('contactId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('emailId', models.CharField(max_length=50)),
                ('question', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventID', models.IntegerField()),
                ('EventName', models.CharField(blank=True, max_length=100)),
                ('EventDescription', models.CharField(max_length=100)),
                ('EventTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('EventLocation', models.CharField(max_length=100)),
                ('CoordinatorID', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]