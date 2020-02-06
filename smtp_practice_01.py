#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.sina.com"  #设置服务器
mail_user="ygqs"    #用户名
mail_pass=input('input your passport')
 
 
sender = 'ygqs@sina.com'
receivers = ['ygqs@sina.com']  # 接收邮件
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("ygqs", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
#except smtplib.SMTPException:
except Exception as e:
    print ("Error: 无法发送邮件",e)

