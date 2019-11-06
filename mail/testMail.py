
from utils import log
from mail import Mail


def test_mail(to_addr, mail_content, mail_subject):
    mail = Mail()
    mail.add_sender_and_content(to_addr,mail_content, mail_subject)
    mail_dict = mail.__dict__
    log(mail_dict)
    mail.send_mail()


if __name__ == '__main__':
    to_addr = "zhengchen@wayyue.com"
    mail_content = "mail_content"
    mail_subject = "python监控"
    test_mail(to_addr, mail_content, mail_subject)




