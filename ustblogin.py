#!/usr/bin/env python
# coding:utf-8

import urllib
import urllib2
import socket
import netifaces


STUID = ''
STUPASS = ''

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


def main():
    v6ip = getv6ip()
    v6ip = '2001:da8:208:21b:8d16:5863:fdc2:f1d5'

    addrs = netifaces.ifaddresses('wlan0')
    v6ip = addrs[netifaces.AF_INET6][0]['addr']

    data = {'DDDDD': STUID, 'upass': STUPASS, '0MKKey': '123456789', 'v6ip': v6ip}
    request = urllib2.Request(url, urllib.urlencode(data))
    response = urllib2.urlopen(request)
    print response.getcode()

if __name__ == '__main__':
    main()
