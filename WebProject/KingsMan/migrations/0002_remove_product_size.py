# Generated by Django 2.1.1 on 2018-10-21 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KingsMan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
