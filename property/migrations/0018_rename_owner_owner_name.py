# Generated by Django 3.2.12 on 2024-08-27 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_alter_owner_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
    ]