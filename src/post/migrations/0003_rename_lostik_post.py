# Generated by Django 4.0 on 2024-02-24 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_post_lostik'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lostik',
            new_name='Post',
        ),
    ]