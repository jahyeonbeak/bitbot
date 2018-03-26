#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jahyeonbeak@gmail.com
# date:   2018-03-21
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../BitcoinMonitor/scripts/api').replace('\\', '/'))
from bithumb.easy_api import EasyAPI
import json

class ApiManager(object):
    '''
    '''
    def __init__(self):
        #self._url = config.PRICE_INTERFACE['huobi']
        #self._request_timeout = int(config.REQUEST_TIMEOUT)
        self._name = 'api_manager'

        self.bithumb_api=EasyAPI('e10a77523a6951f37b20526a86e8bc74','b477aa50c9c46530dc310e5dd76708be');
        #self.okcoinSpot = OKCoinSpot(config.OKCOIN_RESTURL,'','')

    @property
    def name(self):
        return self._name

    def query(self):
        try:
            print('bithumb price updater')
            #账户信息
            resa = self.bithumb_api.get_account()
            print (resa)
            #账户余额
            res = self.bithumb_api.get_balance(currency='BTC')
            print (res)
            res = self.bithumb_api.get_my_transactions()
            print(res)
            a = json.dumps(resa)
            return a
        except Exception as e:
            print (e)
            #logger.error('Error: %s' % str(e))
            return "None"
    def GetBithumbApi(self):
        return self.bithumb_api
    pass

def main():

    p = ApiManager()
    p.query()
    pass

if __name__ == '__main__':
    main()
