import os
import sys
import smtplib
from email.mime.text import MIMEText
import ConfigParser
import datetime
import time
import logging
import csv

def send_mail(cfgfile, email, messages):
    logging.info('Send email to %s.' % email)
    #mailto_list=["aaa@your.com"]
    #mail_host="smtp.gmail.com:587"
    #mail_user="youraccount"
    #mail_pass="yourpassword"
    #mail_postfix="gmail.com"
    sub = 'Say hello to you from program!'
    config = ConfigParser.RawConfigParser()
    config.read(cfgfile)
    mail_host = config.get('mail','mail_host')
    mail_user = config.get('mail','mail_user')
    mail_pass = config.get('mail','mail_pass')
    mail_postfix = config.get('mail','mail_postfix')
    #mail_from = config.get('mail','mail_from')
    to_list = [email,]
    #to_list.append(config.get('mail','mailto_list'))
    #print mailto_list

    #content = os.linesep.join(messages)
    content = messages
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
    fin = open('new.csv')
    fout = open('master.csv', 'ab')
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    reader.next()
    for row in reader:
        #print row
        content = 'Missing content file.'
        with open('email-content.txt') as f:
            content = f.read()
        email = row[-2]
        if email:
            ###
            #r = send_mail('sendemail-lhz.ini', email, content)
            r = send_mail('sendemail.ini', email, content)
            if r:
                row[-1] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow(row)

    fin.close()
    fout.close()
    print 'Completed in', time.clock() - start_time, 'seconds'

if __name__ == '__main__':
    main()
