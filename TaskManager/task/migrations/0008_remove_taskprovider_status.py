# Generated by Django 3.2.6 on 2022-06-08 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_taskprovider_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskprovider',
            name='status',
        ),
    ]