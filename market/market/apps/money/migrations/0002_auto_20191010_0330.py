# Generated by Django 2.2.5 on 2019-10-10 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='name',
            field=models.TextField(default='', max_length=50, verbose_name='名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='money',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='描述'),
        ),
    ]
