# Generated by Django 2.0 on 2019-09-12 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20190911_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crabimage',
            name='crab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='market.Crab'),
        ),
        migrations.AlterField(
            model_name='crabimage',
            name='pic',
            field=models.ImageField(upload_to='img/crab_images/', verbose_name='图片'),
        ),
    ]
