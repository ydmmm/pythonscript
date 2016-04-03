from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
from_addr = '18781908309@163.com'
password = 'wyxdym11171014'
to_addr = '1006248405@qq.com'
smtp_server = 'smtp.163.com'
msg = MIMEText('hello,儿子','plain','utf-8')
msg['From'] = _format_addr('Your father <%s>' %from_addr)
msg['Subject'] = Header('来自your father 的问候','utf-8').encode()
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

