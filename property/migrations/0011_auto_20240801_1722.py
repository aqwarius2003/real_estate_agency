# Generated by Django 2.2.24 on 2024-08-01 13:22

from django.db import migrations


def copy_owners_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()

    for flat in flats.iterator():
        owner, created = Owner.objects.get_or_create(
            owner=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone,
        )
        owner.flats.add(flat)
        owner.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(copy_owners_data)
    ]
