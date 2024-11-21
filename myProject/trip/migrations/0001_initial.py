# Generated by Django 5.1.1 on 2024-11-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('addr1', models.CharField(max_length=255)),
                ('addr2', models.CharField(blank=True, max_length=255)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='trip_images/')),
                ('weather_info', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
    ]