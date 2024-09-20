# Generated by Django 5.1.1 on 2024-09-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='별명'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_num',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='전화번호'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
