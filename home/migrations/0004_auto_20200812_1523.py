# Generated by Django 3.1 on 2020-08-12 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200812_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='smtpemail',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtppassword',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpport',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpserver',
        ),
    ]