# Generated by Django 3.2.12 on 2024-09-01 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20240901_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='likes',
            new_name='likes_by',
        ),
    ]
