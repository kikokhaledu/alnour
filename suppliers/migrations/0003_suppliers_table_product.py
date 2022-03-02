# Generated by Django 3.1.7 on 2022-02-04 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220203_1325'),
        ('suppliers', '0002_suppliers_table_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliers_table',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suplier_product', to='products.products_table'),
        ),
    ]
