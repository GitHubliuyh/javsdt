# -*- coding:utf-8 -*-
import re, requests
from os import system
# from traceback import format_exc


# 用户指定javbook的网址后，请求jav所在网页，返回html
def get_book_html(url, proxy):
    for retry in range(10):
        try:
            if proxy:
                rqs = requests.get(url, proxies=proxy, timeout=(16, 17))
            else:
                rqs = requests.get(url)
        except requests.exceptions.ProxyError:
            # print(format_exc())
            print('    >通过局部代理失败...')
            continue
        except:
            print('    >打开网页失败，重新尝试...')
            continue
        rqs.encoding = 'utf-8'
        rqs_content = rqs.text
        if re.search(r'javbooks', rqs_content):
            return rqs_content
        else:
            print('    >打开网页失败，空返回...重新尝试...')
            continue
    print('>>请检查你的网络环境是否可以打开：', url)
    system('pause')


# 向javbook post车牌，得到jav所在网页，也可能是无结果的网页，返回html
def post_book_html(url, data, proxy):
    for retry in range(10):
        try:
            if proxy:
                rqs = requests.post(url, data=data, proxies=proxy, timeout=(6, 7))
            else:
                rqs = requests.post(url, data=data, timeout=(6, 7))
        except requests.exceptions.ProxyError:
            # print(format_exc())
            print('    >通过局部代理失败，重新尝试...')
            continue
        except:
            # print(format_exc())
            print('    >打开网页失败，重新尝试...')
            continue
        rqs.encoding = 'utf-8'
        rqs_content = rqs.text
        if re.search(r'Javbooks', rqs_content):
            return rqs_content
        else:
            print('    >打开网页失败，空返回...重新尝试...')
            continue
    print('>>请检查你的网络环境是否可以打开：', url)
    system('pause')

