# Generated by Django 3.2.19 on 2023-12-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
    ]
