# Generated by Django 2.2.5 on 2019-11-16 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0021_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avail_date', models.DateField()),
                ('start_time', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Doctor')),
            ],
        ),
    ]
