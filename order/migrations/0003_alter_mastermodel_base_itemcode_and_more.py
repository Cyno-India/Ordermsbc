# Generated by Django 4.1.2 on 2022-10-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_mastermodel_alter_order_orderfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastermodel',
            name='Base_ItemCode',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='mastermodel',
            name='Ordered_ItemCode',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='mastermodel',
            name='Particular',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderfile',
            field=models.FileField(upload_to=''),
        ),
    ]