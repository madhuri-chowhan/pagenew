# Generated by Django 3.2.9 on 2021-11-16 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0008_remove_accessrecord_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_one.web'),
        ),
    ]
