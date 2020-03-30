#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import get_ip


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


url='https://www.xicidaili.com/nn'
ip=get_ip.get_random_ip()
html=requests.get(url=url,headers=headers,proxies=ip).text
print(html)
print(ip)