# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

from Public.pyreport_excel import create
import os
import datetime
from testCase.case import testinterface
from Public.get_excel import datacel
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib


def start_excel_report_http():
    # m = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    m = datetime.datetime.now().strftime("%Y%m%d")
    basdir = os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '\\test_case_data\\case.xlsx'
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path)
    listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi = testinterface()
    filepath = os.path.join(basdir + '\\test_Report\\%s-result-us.xls' % m)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    create(filename=filepath, list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey, listconeents=listconeent, listfangshis=listfangshi, listqiwangs=listqiwang,
           listids=listid, listrelust=listrelust, listnames=listname)
    #  邮箱配置
    sender = 'jtsz2010@163.com'
    psw = 'lovejt333'
    # 收件人多个时，中间用逗号隔开,如'a@xx.com,b@xx.com'
    receiver = 'jtsz2010@163.com', '15814405932@139.com', 'jiangtao02@hnjing.com'
    # receiver_mail = {'mail': 'jtsz2010@163.com, jiangtao02@hnjing.com, 348000842@qq.com'}

    smtp_server = 'smtp.163.com'
    send_mail(sender, psw, receiver, smtp_server, filepath)


def send_mail(sender, psw, receiver, smtpserver, filepath):
    # 读取测试报告的内容
    with open(filepath, "rb") as f:
        mail_body = f.read()
        # 定义邮件内容
        msg = MIMEMultipart()
        body = MIMEText('各位亲，以上附件是接口测试相关信息，请知悉！', 'plain', _charset='utf-8')
        msg['Subject'] = u"这是一份测试报告"
        msg["from"] = sender
        msg["to"] = psw
        # 加上时间戳
        # msg["date"] = time.strftime('%a, %d %b %Y %H_%M_%S %z')
        msg.attach(body)
        # 添加附件
        xlsxpart = MIMEApplication(open(filepath, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename=filepath)
        msg.attach(xlsxpart)
        # 登录邮箱
        smtp = smtplib.SMTP()
        # 连接邮箱服务器
        smtp.connect(smtpserver)
        # 用户名密码
        smtp.login(sender, psw)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('test report email has send out !')


if __name__ == '__main__':
    start_excel_report_http()
