#!/usr/bin/env python
# coding:utf-8

"""
Make computer always online.

"""

import urllib
import urllib2
import socket
import netifaces
import time
import schedule


STUID = ''
STUPASS = ''


def internet_on():
    """
    check if internet_on
    """
    try:
        response = urllib2.urlopen('http://baidu.com', timeout=1)
        html = response.read()
        if html.startswith('<html>'):
            return True
        else:
            return False
    except urllib2.URLError as err: 
        return False



def getv6ip():
    if socket.has_ipv6:
        addrinfos = socket.getaddrinfo(socket.gethostname(), 80, 0, 0, socket.IPPROTO_TCP)
        for addrinfo in addrinfos:
            print 'addrsinfos: ', addrinfo
            if addrinfo[4][0].startswith('2001'):
                return addrinfo[4][0]
        print('no thing')
    else:
        print 'NO IPV6'

url = 'http://202.204.48.82/'


def connect_internet():
    v6ip = getv6ip()
    v6ip = '2001:da8:208:21b:8d16:5863:fdc2:f1d5'

    addrs = netifaces.ifaddresses('wlan0')
    v6ip = addrs[netifaces.AF_INET6][0]['addr']

    data = {'DDDDD': STUID, 'upass': STUPASS, '0MKKey': '123456789', 'v6ip': v6ip}
    request = urllib2.Request(url, urllib.urlencode(data))
    response = urllib2.urlopen(request)
    print response.getcode()


def schedule_connect():

    def check_internet():
        if internet_on():
            return
        else:
            connect_internet()

    schedule.every(10).to(20).minutes.do(check_internet)

    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    schedule_connect()
