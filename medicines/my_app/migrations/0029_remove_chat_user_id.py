# Generated by Django 2.2.5 on 2020-02-19 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0028_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='user_id',
        ),
    ]
