#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
import requests

# import sys
# import os

# path = sys.argv[0]  # 获取本文件路径
# filename = os.path.basename(path)  # 获取本文件名
# path = os.path.dirname(os.path.realpath(sys.argv[0]))  # 获取本文件所在目录

# filelist = os.listdir(path)  # 获取文件名列表
# # filelist.remove(filename)  # 从目录的文件里面去除本文件的文件名

# print(path)
# print(filename)
# print(path)
# print(filelist)
# print('==============================')

parser = argparse.ArgumentParser(description='获取IP地址DEMO')
parser.add_argument('-i', '--ip', help='获取IP地址', action='store_true')
parser.add_argument('-v', '--version', help='取当前应用版本号', action='store_true')
ages = parser.parse_args()


def get_ip_parse():
    print('正在解析当前IP中,请稍后....')
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    }

    params = {
        'json': 'true',
    }

    response = requests.get('http://whois.pconline.com.cn/ipJson.jsp', params=params, headers=headers, verify=False).json()
    # print(response)
    # print('IP地址:', response['ip'], '\n城市:', response['city'], '\n类型:', response['addr'])
    return {'ip': response['ip'], 'city': response['city'], 'addr': response['addr']}


if __name__ == '__main__':
    if ages.ip:
        print(get_ip_parse())
    elif ages.version:
        print('0.0.1')
    else:
        print('请输入参数 -i 或 -v')