# Generated by Django 4.2.1 on 2023-06-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("suppliers", "0003_supplier_total_provided_from_supplier"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplierbatch",
            name="weight",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
