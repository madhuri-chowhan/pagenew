# Generated by Django 3.2.9 on 2021-11-16 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0007_accessrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='name',
        ),
    ]