# Generated by Django 2.0 on 2018-04-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20180405_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskrecord',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
