# Generated by Django 2.1.2 on 2019-01-02 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commission',
            old_name='Currentday',
            new_name='currentday',
        ),
    ]
