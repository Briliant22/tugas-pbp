# Generated by Django 4.2.4 on 2023-09-18 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
    ]
