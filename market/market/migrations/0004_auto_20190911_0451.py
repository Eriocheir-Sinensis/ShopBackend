# Generated by Django 2.2.5 on 2019-09-11 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20190911_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0, verbose_name='数量')),
                ('crab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Crab')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '购物车', 'verbose_name_plural': '购物车'},
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Customer')),
                ('line_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_items', to='market.LineItem')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
    ]
