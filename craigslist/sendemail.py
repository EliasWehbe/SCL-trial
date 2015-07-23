import os
import sys
import smtplib
from email.mime.text import MIMEText
import ConfigParser

import logging

def send_mail(cfgfile, messages):
    logging.info('Send alerts email.')
    #mailto_list=["aaa@your.com"]
    #mail_host="smtp.gmail.com:587"
    #mail_user="youraccount"
    #mail_pass="yourpassword"
    #mail_postfix="gmail.com"
    sub = 'Error alerts from get_reports program!'
    config = ConfigParser.RawConfigParser()
    config.read(cfgfile)
    mail_host = config.get('mail','mail_host')
    mail_user = config.get('mail','mail_user')
    mail_pass = config.get('mail','mail_pass')
    mail_postfix = config.get('mail','mail_postfix')
    #mail_from = config.get('mail','mail_from')
    to_list = []
    to_list.append(config.get('mail','mailto_list'))
    #print mailto_list

    content = os.linesep.join(messages)
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    #msg['To'] = to_list
    try:
        #s = smtplib.SMTP()
        #s.connect(mail_host)
        s = smtplib.SMTP(mail_host)
        s.starttls()
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        #s.close()
        s.quit()
        return True
    except Exception, e:
        #print str(e)
        logging.error('Send mail error :%s' % (e))
        return False

def main():
    #os.system('dir')
    start_time = time.clock()
    logging.basicConfig(filename='logging.txt', format="%(asctime)s;%(levelname)s;%(message)s", level=logging.DEBUG)
    logging.info('Start to send emails...')
    send_mail('sendemail.ini', 'test')
    print 'Completed in', time.clock() - start_time, 'seconds'

if __name__ == '__main__':
    main()
