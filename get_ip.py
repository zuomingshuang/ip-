import requests
from bs4 import BeautifulSoup
import lxml
import random

#文档：1、该模块可以随机获取代理IP  2、使用方法：导入该模块，然后调用模块的get_random_ip()方法，此方法无参数

url='https://www.xicidaili.com/nn' #代理IP首页地址
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def get_ip_list(url,headers):
    ip_list=[]
    html=requests.get(url=url,headers=headers).text
    soup=BeautifulSoup(html,'lxml')
    table=soup.find('table',attrs={'id':'ip_list'})
    tr_list=table.find_all('tr')
    for tr in tr_list[1:]:
        td_list=tr.find_all('td')
        ip='http://'+td_list[1].text+':'+td_list[2].text
        ip_list.append(ip)
    return ip_list

def get_random_ip():
    ip=random.choice(get_ip_list(url,headers))
    proxies={'http':ip}
    return proxies

#以下是测试代码
if __name__=='__main__':
    proxies=get_random_ip()
    print(proxies)
    html=requests.get(url=url,headers=headers,proxies=proxies).text
    print(html)

