#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jahyeonbeak@gmail.com
# date:   2018-04-17

class DualPlatformHedging(object):
    '''
    参数               默认值  描述
    ------------    ------  --------
    MinSpreadA      0.51    A->B差价
    MinSpreadB      0.52    B->A差价
    MaxAmount       0.3     最大操作量
    BalanceTime     10      平衡周期(秒)
    LoopInterval    200     轮询周期(ms)
    '''

    MarketA = {'fee':''}


    def __init__(self):
        self.MinSpreadA2B = 0.51
        self.MinSpreadB2A = 0.01
        self.MaxAmount = 1

        self.buy_priceA = 0
        self.buy_priceB = 0


        pass

    def _trade_conditions(self):
        if self.sell_priceA > self.buy_priceB:
            #判断从A卖出同事从B买入是否有利润
            pass
        elif self.sell_priceB > self.buy_priceA:
            # 判断从B卖出同事从A买入是否有利润
            pass

    def _margin_calculate(self, buy, sell, buy_fee, sell_fee, base_coin, base_ustd):
        buy_amount_price = self.MaxAmount * (buy + buy * buy_fee) #买入总价
        sell_amount_coin = self.MaxAmount * (sell - sell * sell_fee) #卖出总价
        is_can_buy = sell_amount_coin > base_coin
        is_can_sell = buy_amount_price > base_ustd
        if is_can_buy and is_can_sell:
            return True
        else:
            return False

    def _value_test(self):
        return self.MinSpreadB2A

    def _run_strategy(self):
        pass

    def _run_loopback_testing(self):
        pass

    pass

def main():
    afa = DualPlatformHedging()
    print (afa._value_test())

    pass

if __name__ == '__main__':
    main()