from django.db import models

# Create your models here.

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class TestData(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __unicode__(self):
        return self.lastname

class AccountBalance(models.Model):
    coin = models.CharField(max_length=50) #币种
    in_use = models.FloatField(default=0) #使用中资产
    total = models.FloatField(default=0)#总资产
    misu = models.FloatField(default=0)
    available = models.FloatField(default=0) #可用资产

    def __unicode__(self):
        return self.coin


class TradeHistory(models.Model):
    transfer_date = models.DateTimeField(auto_now_add=False) #时间戳
    exchange = models.FloatField(default=0) #使用中资产
    type = models.IntegerField(default=0)
    units = models.FloatField(default=0) #使用中资产
    price = models.FloatField(default=0) #使用中资产
    fee = models.FloatField(default=0) #使用中资产
    coin_remain = models.FloatField(default=0) #使用中资产
    krw_remain = models.FloatField(default=0) #使用中资产

    def __unicode__(self):
        return self.transfer_date
