# Generated by Django 2.0.2 on 2018-03-29 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arbitrage', '0002_testdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('coin', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('in_use', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('misu', models.FloatField(default=0)),
                ('available', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TradeHistory',
            fields=[
                ('transfer_date', models.DateTimeField(primary_key=True, serialize=False)),
                ('exchange_rate', models.FloatField(default=0)),
                ('trade_type', models.IntegerField(default=0)),
                ('trade_units', models.FloatField(default=0)),
                ('trade_price', models.FloatField(default=0)),
                ('trade_fee', models.FloatField(default=0)),
                ('coin_remain', models.FloatField(default=0)),
                ('krw_remain', models.FloatField(default=0)),
                ('trade_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrage.AccountBalance')),
            ],
        ),
    ]