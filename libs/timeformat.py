#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jahyeonbeak@gmail.com
# date:   2018-04-18

from rfc3339 import rfc3339
import datetime

def timestamp2rfc3339(ts):
    d = datetime.datetime.fromtimestamp(timestamp(ts))
    r = rfc3339(d, utc=True, use_system_timezone=True)
    return r

def timestamp2string(ts):
    try:
        d = datetime.datetime.fromtimestamp(timestamp(ts))
        str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
        # 2015-08-28 16:43:37.283000'
        return str1
    except Exception as e:
        print (e)
        return ''

def timestamp(ts):
    if len(str(ts)) == 13:
        return float(ts/1000)
    elif len(str(ts)) == 10:
        return ts
    else:
        return 0

def main():
    print (timestamp2rfc3339(1524040817889))
    pass

if __name__ == '__main__':
    main()