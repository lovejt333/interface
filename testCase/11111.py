import requests
from Public.login import testlogin_001

token = testlogin_001().test_login_001("token")
headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': token
        }
params = {
    "pageSize": "1000",
    "isShowUndis": "1"
}
print(type(params))
if params == "data":
    print("这是data数据类型")
elif params == "json":
    print("这是json数据")
else:
    print("没有对应的数据类型")
# s = requests.get("http://sp.ejw.cn/os/v1/partner/190/departments?pageSize=1000&isShowUndis=1", headers=headers)
s = requests.get("http://sp.ejw.cn/os/v1/partner/190/departments?", params=params, headers=headers)
# print(s.content.decode("utf-8"), type(s.content.decode("utf-8")))

departName = "市场二部"
if departName in s.content.decode("utf-8"):
    print(departName+"判断正确")
else:
    print(departName+"没有查询到此信息")

