# -*- coding: utf-8 -*-# @Time    : 2018/3/18 09:36# @Author  : jt# @Site    :# @File    : test_requests.pyimport requestsimport jsonfrom Public.log import LOG, loggerfrom Public.login import testlogin_001token = testlogin_001().test_wwwlogin('token')@logger('requests封装')class requ():    def __init__(self):        self.headers = {            'Content-Type': 'application/json;charset=UTF-8',            'token': token        }    def get(self, url, params):  # get消息        # params = json.dumps(params)        try:            r = requests.get(url, params=params, headers=self.headers)            r.encoding = 'UTF-8'            json_response = r.status_code            json_response_text = r.content.decode("utf-8")            return {'code': 0, 'result': json_response, 'result_act': json_response_text}        except Exception as e:            LOG.info('get请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}    def post(self, url, params):  # post消息        try:            r = requests.post(url, data=params, headers=self.headers)            r.encoding = 'UTF-8'            json_response = r.status_code            # json_response_text = json.loads(r.text, encoding="utf-8")            json_response_text = r.content.decode("utf-8")            return {'code': 0, 'result': json_response, 'result_act': json_response_text}        except Exception as e:            LOG.info('post请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}    def delfile(self, url, params):  # 删除的请求        try:            r = requests.delete(url, data=params, headers=self.headers)            json_response = r.status_code            json_response_text = r.content.decode("utf-8")            return {'code': 0, 'result': json_response, 'result_act': json_response_text}        except Exception as e:            LOG.info('del请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}    def putfile(self, url, params):  # put请求        try:            data = json.dumps(params)            r = requests.put(url, data, headers=self.headers)            json_response = r.status_code            json_response_text = r.content.decode("utf-8")            return {'code': 0, 'result': json_response, 'result_act': json_response_text}        except Exception as e:            LOG.info('put请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}