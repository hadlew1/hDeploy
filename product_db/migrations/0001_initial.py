# Generated by Django 2.2.16 on 2020-11-02 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.TextField()),
                ('supplier_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='purchase_order',
            fields=[
                ('purchase_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now=True)),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_db.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='product_purchase_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_db.product')),
                ('purchase_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_db.purchase_order')),
            ],
        ),
    ]
