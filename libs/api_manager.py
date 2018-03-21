#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jahyeonbeak@gmail.com
# date:   2018-03-21
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../BitcoinMonitor/scripts/api').replace('\\', '/'))
from bithumb.easy_api import EasyAPI

class ApiManager(object):
    '''
    '''
    def __init__(self):
        #self._url = config.PRICE_INTERFACE['huobi']
        #self._request_timeout = int(config.REQUEST_TIMEOUT)
        self._name = 'api_manager'

        self.bithumb_api=EasyAPI('5408b0d33c37dddb0c503049634de550','642f0489577c852e20a91c10d7abf245');
        #self.okcoinSpot = OKCoinSpot(config.OKCOIN_RESTURL,'','')

    @property
    def name(self):
        return self._name

    def query(self):
        try:
            print('bithumb price updater')
            #账户信息
            res = self.bithumb_api.get_account()
            print (res)
            #账户余额
            res = self.bithumb_api.get_balance()
            print (res)
            res = self.bithumb_api.get_my_transactions()
            print(res)
            return True
        except Exception as e:
            print (e)
            #logger.error('Error: %s' % str(e))
            return False
    def GetBithumbApi(self):
        return self.bithumb_api
    pass

def main():

    p = ApiManager()
    p.query()
    pass

if __name__ == '__main__':
    main()
