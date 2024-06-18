# Generated by Django 5.0.6 on 2024-06-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_historicaltask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltask',
            name='status',
            field=models.CharField(choices=[('N', 'NEW'), ('IP', 'IN PROGRESS'), ('R', 'RESOLVED')], default='N', max_length=15),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('N', 'NEW'), ('IP', 'IN PROGRESS'), ('R', 'RESOLVED')], default='N', max_length=15),
        ),
    ]
