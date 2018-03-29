#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jahyeonbeak@gmail.com
# date:   2018-03-21
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../BitcoinMonitor/scripts/api').replace('\\', '/'))
from bithumb.easy_api import EasyAPI
import json
from . import config
#import config


class ApiManager(object):
    '''
    '''
    def __init__(self):
        #self._url = config.PRICE_INTERFACE['huobi']
        #self._request_timeout = int(config.REQUEST_TIMEOUT)
        self._name = 'api_manager'

        self.bithumb_api=EasyAPI(config.BITHUMB_CONNECT_KEY,config.BITHUMB_SECRET_KEY);
        #self.okcoinSpot = OKCoinSpot(config.OKCOIN_RESTURL,'','')

    @property
    def name(self):
        return self._name

    def query(self):
        try:
            print('bithumb price updater')
            #账户信息
            #resa = self.bithumb_api.get_account()
            #print (resa)
            #账户余额
            res = self.bithumb_api.get_balance(currency='ALL')
            #print (res)
            #res = self.bithumb_api.get_my_transactions()
            #print(res)
            a = json.dumps(res)
            return a
        except Exception as e:
            print (e)
            #logger.error('Error: %s' % str(e))
            return "None"

    def _get_trade_history(self):
        res = self.bithumb_api.get_my_transactions(currency='BTC')
        res_data = json.dumps(res)
        res_data = {'status': '0000', 'data': [{'price': '-16801000', 'btc1krw': '0', 'search': '5', 'fee': '1000 KRW', 'transfer_date': '1521798752674957', 'btc_remain': '0.861699', 'units': '0', 'krw_remain': '94714'}, {'price': '16372150', 'btc1krw': '9502000', 'search': '2', 'fee': '3597 KRW', 'transfer_date': '1521798342027665', 'btc_remain': '0.861699', 'units': '- 1.7234', 'krw_remain': '16895714'}, {'price': '-17000000', 'btc1krw': '0', 'search': '5', 'fee': '1000 KRW', 'transfer_date': '1521795736795632', 'btc_remain': '2.585099', 'units': '0', 'krw_remain': '523564'}, {'price': '0', 'btc1krw': '0', 'search': '4', 'fee': '0.0', 'transfer_date': '1521795362952811', 'btc_remain': '2.585099', 'units': '+ 2.585', 'krw_remain': '17523564'}, {'price': '16973026', 'btc1krw': '9430000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521789081682463', 'btc_remain': '0.000099', 'units': '- 1.79989671', 'krw_remain': '17523564'}, {'price': '472474', 'btc1krw': '9430000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521789074852318', 'btc_remain': '1.79999571', 'units': '- 0.05010329', 'krw_remain': '550538'}, {'price': '-6931000', 'btc1krw': '0', 'search': '5', 'fee': '1000 KRW', 'transfer_date': '1521782737622558', 'btc_remain': '1.850099', 'units': '0', 'krw_remain': '78064'}, {'price': '4374757', 'btc1krw': '9446000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521779251737105', 'btc_remain': '1.850099', 'units': '- 0.46313324', 'krw_remain': '7009064'}, {'price': '136653', 'btc1krw': '9446000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521779251446077', 'btc_remain': '2.31323224', 'units': '- 0.01446676', 'krw_remain': '2634307'}, {'price': '2421954', 'btc1krw': '9446000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521779249608237', 'btc_remain': '2.327699', 'units': '- 0.2564', 'krw_remain': '2497654'}, {'price': '-5786000', 'btc1krw': '0', 'search': '5', 'fee': '1000 KRW', 'transfer_date': '1521690767466175', 'btc_remain': '2.584099', 'units': '0', 'krw_remain': '75700'}, {'price': '0', 'btc1krw': '0', 'search': '4', 'fee': '0.0', 'transfer_date': '1521688322350507', 'btc_remain': '2.584099', 'units': '+ 2.584', 'krw_remain': '5861700'}, {'price': '440880', 'btc1krw': '10020000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521685995307430', 'btc_remain': '0.000099', 'units': '- 0.044', 'krw_remain': '5861700'}, {'price': '5010000', 'btc1krw': '10020000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521685993563447', 'btc_remain': '0.044099', 'units': '- 0.5', 'krw_remain': '5420820'}, {'price': '410820', 'btc1krw': '10020000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521685989335165', 'btc_remain': '0.544099', 'units': '- 0.041', 'krw_remain': '410820'}, {'price': '-45837795', 'btc1krw': '0', 'search': '5', 'fee': '1000 KRW', 'transfer_date': '1521685931930461', 'btc_remain': '0.585099', 'units': '0', 'krw_remain': '0'}, {'price': '90144', 'btc1krw': '10016000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521684576928731', 'btc_remain': '0.585099', 'units': '- 0.009', 'krw_remain': '45837795'}, {'price': '18924230', 'btc1krw': '10016000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521684576727522', 'btc_remain': '0.594099', 'units': '- 1.8894', 'krw_remain': '45747651'}, {'price': '1007610', 'btc1krw': '10016000', 'search': '2', 'fee': '0 KRW', 'transfer_date': '1521684576471900', 'btc_remain': '2.483499', 'units': '- 0.1006', 'krw_remain': '26823421'}, {'price': '0', 'btc1krw': '0', 'search': '4', 'fee': '0.0', 'transfer_date': '1521683282942180', 'btc_remain': '2.584099', 'units': '+ 2.584', 'krw_remain': '25815811'}]}
        if res_data['status'] is '0000':
            return res_data['data']
        else:
            return None
        pass

    def _get_account_balance(self):
        res = self.bithumb_api.get_balance(currency='ALL')
        res_data = json.dumps(res)
        res_data = {'status': '0000', 'data': {'available_eos': '0.00000000', 'available_etc': '0.00000000', 'misu_bch': 0, 'misu_krw': 0, 'xcoin_last_bch': '938000', 'total_eos': '0.00000000', 'xcoin_last_qtum': '16900', 'in_use_ltc': '0.00000000', 'in_use_xmr': '0.00000000', 'xcoin_last_btc': '8660000', 'xcoin_last_eos': '6760', 'misu_xrp': 0, 'available_btg': '0.00009970', 'in_use_btg': '0.00000000', 'misu_xmr': 0, 'total_krw': 94714, 'total_xmr': '0.00000000', 'available_zec': '0.00000000', 'misu_eos': 0, 'in_use_bch': '0.00000000', 'available_ltc': '0.00000000', 'available_eth': '0.00000000', 'xcoin_last_dash': '380500', 'in_use_eth': '0.00000000', 'misu_qtum': 0, 'in_use_btc': '0.00000000', 'xcoin_last_zec': '230000', 'available_btc': '0.86169900', 'total_icx': '0.00000000', 'total_ltc': '0.00000000', 'available_xrp': '0.00000000', 'in_use_dash': '0.00000000', 'total_btg': '0.00009970', 'xcoin_last_icx': '3007', 'available_xmr': '0.00000000', 'available_icx': '0.00000000', 'misu_btc': '0.00000000', 'available_krw': 94714, 'misu_ltc': 0, 'in_use_krw': 0, 'total_qtum': '0.00000000', 'total_xrp': '0.00000000', 'total_bch': '0.00000000', 'total_btc': '0.86169900', 'available_dash': '0.00000000', 'in_use_eos': '0.00000000', 'total_etc': '0.00000000', 'in_use_etc': '0.00000000', 'total_eth': '0.00000000', 'xcoin_last_xrp': '626', 'xcoin_last_eth': '487000', 'xcoin_last_xmr': '219200', 'xcoin_last_btg': '57200', 'xcoin_last_etc': '17530', 'misu_icx': 0, 'misu_btg': 0, 'misu_dash': 0, 'xcoin_last_ltc': '143300', 'available_bch': '0.00000000', 'available_qtum': '0.00000000', 'in_use_icx': '0.00000000', 'misu_zec': 0, 'misu_eth': 0, 'in_use_xrp': '0.00000000', 'in_use_zec': '0.00000000', 'in_use_qtum': '0.00000000', 'total_zec': '0.00000000', 'misu_etc': 0, 'total_dash': '0.00000000'}}
        if res_data['status'] is '0000':
            return res_data['data']
        else:
            return None
        pass


    def GetBithumbApi(self):
        return self.bithumb_api
    pass

def main():

    p = ApiManager()
    p.query()
    pass

if __name__ == '__main__':
    main()
