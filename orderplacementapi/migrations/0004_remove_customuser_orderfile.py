# Generated by Django 4.1.2 on 2022-10-21 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderplacementapi', '0003_alter_customuser_orderfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='orderfile',
        ),
    ]
