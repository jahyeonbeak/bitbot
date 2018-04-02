#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jahyeonbeak@gmail.com
# date:   2018-03-29

import sys, os
import json
from arbitrage.models import *
import datetime
import threading
import time
from django.core import serializers


class DBHelper(object):
    '''
    '''

    def __init__(self):
        self._isThreadRun = False
        self.request = None
        self._update_thread = threading.Thread(target=self._update_data)
        self._update_thread.start()

        self._query_agents = []
        pass

    def _set_request(self, request):
        self.request = request
        pass

    def _append_query_list(self, action):
        self._query_agents.append(action)
        pass

    def _query(self):
        for agent in self._query_agents:
            #logger.info('agent "%s"' % (agent.name))
            # get price
            #exchangedata = {'KRW': {'CNY': 0.0058398, 'USD': 0.00091961}, 'USD': {'CNY': 6.3503, 'KRW': 1087.4}, 'CNY': {'KRW': 171.24, 'USD': 0.15747}}
            #agent.set_exchange(exchangedata)
            ret = agent.query()
            if not ret:
                #logger.error('query failed, skip "%s"' % (agent.name))
                continue
        pass

    @staticmethod
    def _insert_account_balance(b_data):
        coin_index_list = []
        for data_index in list(b_data.keys()):
            if data_index.find("total") > -1:
                # 获得最后一个字符串，为币种
                coin_index = data_index.split('_')
                # 将币种存入list中，结果如 ['eos', 'krw', 'xmr', 'icx']
                coin_index_list.append(coin_index[-1])

        for coin_index in coin_index_list:
            item = BithumbAccountBalance(coin=coin_index)
            item.in_use = b_data["in_use_%s" % coin_index]
            item.total = b_data["total_%s" % coin_index]
            item.misu = b_data["misu_%s" % coin_index]
            item.available = b_data["available_%s" % coin_index]
            # item.xcoin_last = b_data["xcoin_last_%s"%coin_index]
            item.save()
            print(BithumbAccountBalance.objects.all())
        pass

    @staticmethod
    def _insert_trade_history(h_data):
        '''
        输入格式
        [{'price': '4374757', 'btc1krw': '9446000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521779251737105',
         'btc_remain': '1.850099', 'units': '- 0.46313324', 'krw_remain': '7009064'},
        {'price': '136653', 'btc1krw': '9446000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521779251446077',
         'btc_remain': '2.31323224', 'units': '- 0.01446676', 'krw_remain': '2634307'}]
        '''
        for data in h_data:
            trade_coin = ''
            exchange_rate = 0.0
            coin_remain = 0.0
            for key in list(data.keys()):
                if key.find('_remain') > -1 and key is not 'krw_remain':
                    trade_coin = BithumbAccountBalance.objects.get(pk=key.split('_')[0])
                    coin_remain = float(data[key])
                elif key.find('1') > -1:
                    exchange_rate = float(data[key])
            item = BithumbTradeHistory(transfer_date=datetime.datetime.fromtimestamp(int(data['transfer_date'][:-6])),
                                trade_coin=trade_coin, exchange_rate=exchange_rate, trade_type=int(data['search']),
                                trade_units=float(data['units'].replace(' ', '')), trade_price=data['price'],
                                trade_fee=float(data['fee'].split(' ')[0]), coin_remain=coin_remain,
                                krw_remain=data['krw_remain'])
            item.save()
            pass

    def _update_data(self):
        while True:
            data = BithumbTradeHistory.objects.all()
            json_data = serializers.serialize("json", data)
            if self.request is not None:
                self.request.websocket.send(json_data.encode(encoding="utf-8"))
                pass
            time.sleep(5)
        pass



db_helper = DBHelper()
