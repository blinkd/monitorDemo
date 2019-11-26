
from flask_apscheduler import APScheduler
from utils import log
from mail.testMail import test_mail


class Config(object):
    SCHEDULER_API_ENABLED = True


scheduler = APScheduler()


# interval examples
# @scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
# def job1():
#     log('Job 1 executed')


# cron examples
@scheduler.task('cron', id='do_job_2', minute='*/59')
def job2():
    log('Job 2 executed')
    to_addr = "zhengchen@wayyue.com"
    mail_content = "mail_content"
    mail_subject = "python监控"
    test_mail(to_addr, mail_content, mail_subject)


@scheduler.task('cron', id='do_job_3', week='*', day_of_week='sun')
def job3():
    log('Job 3 executed')