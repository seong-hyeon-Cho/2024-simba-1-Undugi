# Generated by Django 5.0.6 on 2024-06-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='daily_consumedCalorie',
            field=models.FloatField(default=0, null=True),
        ),
    ]
