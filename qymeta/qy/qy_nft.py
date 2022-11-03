#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/10/27 17:29
# @Author : justin.郑 3907721@qq.com
# @File : qy_nft.py
# @desc : 清元链NFT接口

import json
import time
import requests
from qymeta.utils.sign import qy_sign

http_url = 'http://qymeta_api.newmin.cn/api/'
headers = {'Content-Type': 'multipart/form-data'}


# 创建链账户
def qy_nft_create_account_address(appid: str, secret: str, name: str, idc: str, mobile: str) -> dict:
    interface_name = 'createAccountAddress'
    h_url = http_url + interface_name

    data = {
        'appid': appid,
        'secret': secret,
        'name': name,
        'idc': idc,
        'mobile': mobile,
        'timestamp': str(int(time.time()))
    }
    data['sign'] = qy_sign(data)
    r = requests.post(url=h_url, data=data, headers=headers)
    return json.loads(r.text)


# 创建NFT资源
def qy_nft_create_nft(appid: str, secret: str, title: str, author: str, url: str, address: str, series_name: str = '', series_id: str = ''):
    interface_name = 'createNft'
    h_url = http_url + interface_name

    data = {
        'appid': appid,
        'secret': secret,
        'title': title,
        'author': author,
        'address': address,
        'url': url,
        'series_id': series_id,
        'series_name': series_name,
        'timestamp': str(int(time.time()))
    }
    data['sign'] = qy_sign(data)
    r = requests.post(url=h_url, data=data, headers=headers)
    return json.loads(r.text)


# 铸造NFT
def qy_nft_casting_nft(appid: str, secret: str, order_sn: str, source_url: str):
    interface_name = 'save'
    h_url = http_url + interface_name

    data = {
        'appid': appid,
        'secret': secret,
        'order_sn': order_sn,
        'source_url': source_url,
        'timestamp': str(int(time.time()))
    }
    data['sign'] = qy_sign(data)
    r = requests.post(url=h_url, data=data, headers=headers)
    return json.loads(r.text)


# NFT转移
def qy_nft_trans_from(appid: str, secret: str, address_from: str, address_to: str, token_id: str):
    interface_name = 'transFrom'
    h_url = http_url + interface_name

    data = {
        'appid': appid,
        'secret': secret,
        'address_from': address_from,
        'address_to': address_to,
        'token_id': token_id,
        'timestamp': str(int(time.time()))
    }
    data['sign'] = qy_sign(data)
    r = requests.post(url=h_url, data=data, headers=headers)
    return json.loads(r.text)


# 查询某账户拥有的NFT
def qy_nft_get_balanceof(appid: str, secret: str, address: str):
    interface_name = 'getBalanceof'
    h_url = http_url + interface_name

    data = {
        'appid': appid,
        'secret': secret,
        'address': address,
        'timestamp': str(int(time.time()))
    }
    data['sign'] = qy_sign(data)
    r = requests.post(url=h_url, data=data, headers=headers)
    return json.loads(r.text)


# 查询NFT上链存证信息
def qy_nft_query(appid: str, secret: str, hash: str):
    interface_name = 'query'
    h_url = http_url + interface_name

    data = {
        'appid': appid,
        'secret': secret,
        'hash': hash,
        'timestamp': str(int(time.time()))
    }
    data['sign'] = qy_sign(data)
    r = requests.post(url=h_url, data=data, headers=headers)
    return json.loads(r.text)


# 销毁NFT
def qy_nft_destruction(appid: str, secret: str, address_from: str, token_id: str):
    interface_name = 'destruction'
    h_url = http_url + interface_name

    data = {
        'appid': appid,
        'secret': secret,
        'address_from': address_from,
        'token_id': token_id,
        'timestamp': str(int(time.time()))
    }
    data['sign'] = qy_sign(data)
    r = requests.post(url=h_url, data=data, headers=headers)
    return json.loads(r.text)


if __name__ == "__main__":
    pass

