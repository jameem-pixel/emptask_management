# Generated by Django 3.2.6 on 2022-06-08 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_remove_taskprovider_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ASSIGNED', 'assigned'), ('INPROGRESS', 'inprogress'), ('HOLD', 'hold'), ('COMPLETED', 'completed')], default='ASSIGNED', max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.employee')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.taskprovider')),
            ],
        ),
    ]
