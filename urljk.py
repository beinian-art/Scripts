#!/usr/bin/env python
-- coding: UTF-8 --
author  libertyspy
link    http://www.lastme.com
import socket
import smtplib
import urllib
mail_options = {
    'server':'smtp.qq.com',#ʹ����QQ��SMTP������Ҫ�����������ÿ���SMTP����
    'port':25,             #�˿�
    'user':'hacker@qq.com',#������
    'pwd':'hacker',        #�����˵�����
    'send_to':'sniper@qq.com',  #�ռ���
}
msg_options={
    'user':'hacker',    #����ƽ̨���û���
    'pwd':'74110',      #����ƽ̨������
    'phone':'12345678910',   #��Ҫ�����ŵĵ绰����
}
test_host = 'http://www.lastme.com/'
def url_request(host,port=80):
    try:
        response = urllib.urlopen(host)
        response_code = response.getcode()
        if 200 != response_code:
            return response_code
        else:
            return True
    except IOError,e:
        return False
def send_message(msg,host,status):
    send_msg='������:%s���ˣ�״̬�룺%s' % (host,status)
    request_api="http://www.uoleem.com.cn/api/uoleemApi?username=%s&pwd=%s&mobile=%s&content=%s&quot;  \
            % (msg['user'],msg['pwd'],msg['phone'],send_msg)
    return url_request(request_api)
def send_email(mail,host,status):
    smtp = smtplib.SMTP()
    smtp.connect(mail['server'], mail['port'])
    smtp.login(mail['user'],mail['pwd'])
    msg="From:%s\rTo:%s\rSubject:������: %s ���� !״̬��:%s\r\n" \
         % (mail['user'],mail['send_to'],host,status)
    smtp.sendmail(mail['user'],mail['send_to'], msg)
    smtp.quit()
"""
def check_status(host,port=80):
    s = socket.socket()
    ret_msg = []
    try:
        s.connect((host,port))
        return True
    except socket.error,e:
        return False
"""
if name=='main':
    status = url_request(test_host)
    if status is not True and status is not None:
        send_email(mail_options,test_host,status)
        send_message(msg_options,test_host,status)
    else:
        pass</pre> 