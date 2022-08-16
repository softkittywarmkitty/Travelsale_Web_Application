# Generated by Django 3.2.13 on 2022-04-19 18:24

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelsale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paymethod',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='travelsale.paymethod'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='travelproduct',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=3),
        ),
        migrations.AlterField(
            model_name='travelproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=15),
        ),
    ]