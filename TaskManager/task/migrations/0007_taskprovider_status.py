# Generated by Django 3.2.6 on 2022-06-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_taskprovider_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskprovider',
            name='status',
            field=models.CharField(choices=[('ASSIGNED', 'assigned'), ('INPROGRESS', 'inprogress'), ('HOLD', 'hold'), ('COMPLETED', 'completed')], default='ASSIGNED', max_length=50),
        ),
    ]
