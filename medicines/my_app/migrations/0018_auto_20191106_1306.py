# Generated by Django 2.2.5 on 2019-11-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0017_tbl_medicalshop_tbl_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.FileField(default='images/member1.png', upload_to='my_app/img/'),
        ),
    ]