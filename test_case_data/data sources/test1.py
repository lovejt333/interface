import yaml

f = open('paas_us_1.2.3.yaml', 'r', encoding='UTF-8')
x = yaml.load(f)
# print(x)
y1 = x["paths"].keys()


# 获取当前第一个请求方法
for method in y1:
    url_01 = "http://sp.ejw.cn/us/v1"
    url_02 = url_01 + method
    y3 = x["paths"][method]
    # y4 = list(y3.values())[0]
    # print(list(y3)[0])
    if len(list(y3)) > 1:
        # print(url_02, list(y3))
        for i in range(0, len(list(y3))):
            print(url_02, list(y3)[i])
    else:
        print(url_02, list(y3)[0])