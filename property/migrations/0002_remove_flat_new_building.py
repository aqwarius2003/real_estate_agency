# Generated by Django 2.2.24 on 2024-07-16 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='new_building',
        ),
    ]
