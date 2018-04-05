# Generated by Django 2.0 on 2018-04-05 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20180405_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='tasks.Task')),
            ],
        ),
    ]
