# Generated by Django 2.2.5 on 2019-09-11 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20190911_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, verbose_name='姓名')),
                ('phone', models.CharField(max_length=80, verbose_name='电话号码')),
                ('address', models.CharField(max_length=300, verbose_name='地址')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
            },
        ),
        migrations.RemoveField(
            model_name='crab',
            name='id',
        ),
        migrations.AddField(
            model_name='crab',
            name='cid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('crabs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crabs', to='market.Crab')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Customer')),
            ],
        ),
    ]
