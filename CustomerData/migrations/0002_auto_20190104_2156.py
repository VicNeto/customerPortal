# Generated by Django 2.1.1 on 2019-01-04 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerData', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fist_Name',
            new_name='first_Name',
        ),
    ]