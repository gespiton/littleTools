import smtplib

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
server = 'smtp.qq.com:465'
qq = '1044750905@qq.com'
aop = 'rscwohjgkrhybegc'
imp = 'knskxdcleycibdef'

smtp = SMTP_SSL(server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(server)
smtp.login(qq, imp)
msg = MIMEText('title', "plain", 'utf-8')
msg["Subject"] = Header('soon', 'utf-8')
msg["From"] = 'movie'
msg["To"] = 'master'
smtp.sendmail(qq, qq, msg.as_string())
smtp.quit()