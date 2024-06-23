# Generated by Django 5.0.3 on 2024-06-22 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickName', models.TextField(max_length=30)),
                ('profileImage', models.ImageField(null=True, upload_to='profileImages/')),
                ('goal', models.FloatField(null=True)),
                ('consumedCalorie', models.FloatField(default=0, null=True)),
                ('weight', models.FloatField(default=50, null=True)),
                ('major', models.TextField(max_length=40)),
                ('gender', models.BooleanField(null=True)),
                ('agegroup', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
