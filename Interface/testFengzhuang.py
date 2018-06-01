# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt
# @Site    : 
# @File    : testFengzhuang.py
from Public.test_requests import requ
import json

reques = requ()


class TestApi(object):
    def __init__(self, url, key, connent, fangshi):
        self.url = url
        self.key = key
        self.connent = json.dumps(connent)
        self.method = fangshi

    def testapi(self):
        if self.method == 'post':
            self.parem = self.connent
            self.response = reques.post(self.url, self.parem)
        elif self.method == 'get':
            self.parem = self.connent
            self.response = reques.get(self.url, self.parem)
        elif self.method == 'put':
            self.parem = self.connent
            self.response = reques.putfile(self.url, self.parem)
        elif self.method == 'delete':
            self.parem = self.connent
            self.response = reques.delfile(self.url, self.parem)
        else:
            raise Exception('没有找到对应的请求方式')
        return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data
