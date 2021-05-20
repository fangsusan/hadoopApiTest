import json
import random

import requests


class Api:

    def url(self):
        url = "http://192.168.0.235:8888"
        return url

    def get_headers(self):
        """用户登陆 获取Authorization值 用于需先登录得接口"""
        data = {
            "username":"fangy",
            "password":111111
        }
        r = requests.post(f"{self.url()}/api/user/auth", json=data)
        print(r.cookies)
        authorization = r.cookies['JSESSIONID']
        headers = {
            "authorization":authorization
        }
        return headers

    def get_adminheaders(self):
        """admin登陆 获取Authorization值 用于权限接口测试"""
        data = {
            "username":"admin",
            "password":"admin"
        }
        r = requests.post(f"{self.url()}/api/user/auth", json=data)
        print(r.cookies)
        authorization = r.cookies['JSESSIONID']
        headers = {
            "authorization":authorization
        }
        return headers


