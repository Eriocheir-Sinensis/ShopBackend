# Generated by Django 2.2.5 on 2019-09-23 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitem',
            name='order',
        ),
    ]
