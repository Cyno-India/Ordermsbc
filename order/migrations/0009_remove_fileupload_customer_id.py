# Generated by Django 4.1.2 on 2022-10-29 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_fileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='customer_id',
        ),
    ]
