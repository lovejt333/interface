# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt
from .log import LOG, logger


@logger('断言测试结果')
def assert_in(asserqiwang, fanhuijson):
    """
    if len(asserqiwang.split('=')) > 1:
        # data = asserqiwang.split('=')
        # 　result = dict([(item.split('=')) for item in data])
        # value1 = ([(str(fanhuijson[key])) for key in result.keys()])
        # value2 = ([(str(value11)) for value11 in result.values()])
        value1 = str(fanhuijson["result"])
        value2 = asserqiwang.split('=')[1]

        if value1 == value2:
            return {'code': 0, "result": 'pass'}
        else:
            return {'code': 1, 'result': 'fail'}
    else:
        LOG.info('填写测试预期值')
        return {"code": 2, 'result': '填写测试预期值'}
    """
    value1 = str(fanhuijson["result"])
    value1_act = asserqiwang.split('=')[1]

    if value1 == value1_act:
        return {'code': 0, "result": 'pass'}
    else:
        return {'code': 1, 'result': 'fail'}

@logger('断言测试结果')
def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('填写测试预期值')
        raise {"code": 1, 'result': '填写测试预期值'}
