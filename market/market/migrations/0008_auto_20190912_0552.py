# Generated by Django 2.0 on 2019-09-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20190912_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crab',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='crab',
            name='net',
            field=models.CharField(default='元', max_length=80, verbose_name='单位'),
        ),
    ]
