# Generated by Django 4.0.2 on 2022-03-03 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='datetime',
        ),
    ]
