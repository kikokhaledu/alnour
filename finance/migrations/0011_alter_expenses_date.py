# Generated by Django 4.0.3 on 2022-03-18 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_po_table_notified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(),
        ),
    ]