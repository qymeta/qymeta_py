#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/10/28 14:07
# @Author : justin.郑 3907721@qq.com
# @File : sign.py
# @desc : 清元链 sign生成

import json
import hashlib


# 清元链 sign生成
def qy_sign(dic: dict) -> str:
    d_list = sorted(dic.items(), key=lambda s: s[0])
    d_dict = dict(d_list)
    d_str = json.dumps(d_dict, separators=(',', ':'))
    d_str = d_str + dic['secret']

    res_1 = hashlib.md5(d_str.encode(encoding='UTF-8')).hexdigest()
    res_2 = hashlib.md5(res_1.encode(encoding='UTF-8')).hexdigest()
    return res_2


if __name__ == '__main__':
    d = {'appid': 'GL0lFgy0AP1I', 'secrect': 'ON4oLiIXNFIe54WCdCZk', 'name': '郑明', 'idc': '420105192200332299', 'mobile': '13377885996', 'timestmp': 1666943811}
    print(qy_sign(d))

