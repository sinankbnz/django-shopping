# Generated by Django 4.1 on 2022-09-21 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productImage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productPrice',
        ),
    ]
