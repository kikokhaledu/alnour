# Generated by Django 4.0.3 on 2022-03-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw_material',
            name='minimum_ammount',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
