# Generated by Django 2.2.5 on 2019-09-26 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]