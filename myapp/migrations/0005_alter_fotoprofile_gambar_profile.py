# Generated by Django 5.1.4 on 2025-02-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_fotoprofile_delete_fotoprofle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotoprofile',
            name='gambar_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
