from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class BithumbAccountBalance(models.Model):
    coin = models.CharField(max_length=50, primary_key=True) #币种
    in_use = models.FloatField(default=0) #使用中资产
    total = models.FloatField(default=0)#总资产
    misu = models.FloatField(default=0)
    available = models.FloatField(default=0) #可用资产
    #xcoin_last = models.FloatField(default=0)

    def __unicode__(self):
        return self.coin


class BithumbTradeHistory(models.Model):
    transfer_date = models.DateTimeField(auto_now_add=False, primary_key=True) #时间戳
    trade_coin = models.ForeignKey(to="BithumbAccountBalance", to_field='coin', null=False, blank=False, on_delete=models.CASCADE)  #币种
    exchange_rate = models.FloatField(default=0) #单笔交易兑换率
    trade_type = models.IntegerField(default=0) #交易类型
    trade_units = models.FloatField(default=0) #交易单位
    trade_price = models.FloatField(default=0) #交易价格
    trade_fee = models.FloatField(default=0) #交易费率
    coin_remain = models.FloatField(default=0) #剩余币数
    krw_remain = models.FloatField(default=0) #剩余资产

    def __unicode__(self):
        return self.transfer_date
