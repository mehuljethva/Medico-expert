# Generated by Django 2.2.5 on 2019-09-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='otp',
            field=models.IntegerField(default=4562),
        ),
    ]
