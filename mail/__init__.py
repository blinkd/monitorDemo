from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class Mail(object):
    def __init__(self):
        self.from_addr = "systemdelivery@wayyue.com"
        self.password = "Way2s2S0#0Z1z58!"
        self.smtp_server = "smtp.exmail.qq.com"
        self.msg = ''
        self.to_addr = ''

    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def add_sender_and_content(self, to_addr, mail_content, subject):
        self.to_addr = to_addr
        msg = MIMEText(mail_content, 'plain', 'utf-8')
        msg['From'] = Mail._format_addr('python监控平台 <%s>' % self.from_addr)
        msg['To'] = Mail._format_addr('<%s>' % to_addr)
        msg['Subject'] = Header(subject, 'utf-8').encode()
        self.msg = msg
        return

    def send_mail(self):
        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()