#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/10/27 17:44
# @Author : justin.郑 3907721@qq.com
# @File : test.py
# @desc : 测试及功能展示


import qymeta as qy

# tmp = qy.qy_nft_create_account_address(
#     appid='GL0lFgy0AP1I',
#     secret='ON4oLiIXNFIe54WCdCZk',
#     name='lisi',
#     idc='420120210303232444',
#     mobile='13377776633',
# )
#
# print(tmp)

# import qymeta as qy
# result = qy.qy_nft_create_nft(appid = "GL0lFgy0AP1I", secret = "ON4oLiIXNFIe54WCdCZk",
#                               title = "cs123", address = '0x24d46c7e149bb540f98c72cdc81bba2d13fb63a8',
#                               author = "ewew ewew", url = "https://pics5.baidu.com/feed/b999a9014c086e06b477fe644dba48ff0bd1cb04.jpeg@f_auto?token=cf5e64232fd162693668f860b5a56ecb")
# print(result)


tmp = qy.qy_nft_casting_nft(
    appid='GL0lFgy0AP1I',
    secret='ON4oLiIXNFIe54WCdCZk',
    source_url='http://openqkl.newmin.cn/resouce/GMC1cNv3PggVtIWsbbjc4sRXiRBUKf',
    order_sn='sasdsffd323'
)

print(tmp)