import email
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class User:

    smtp = "smtp.gmail.com"
    imap = "imap.gmail.com"


    def __init__(self, login, password,subject,recipients,message,header):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message, 'plain'))
        msg['header'] = self.header
        ms = smtplib.SMTP(self.smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login,ms,msg.as_string())
        ms.quit()
#send end

    def recieve(self):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("INBOX")
        criterion = '(HEADER Subject %s)' % (self.header if self.header else 'ALL')
        data = mail.uid('search', None, criterion)
        assert data[0] !='There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()




if __name__ == '__main__':
    user = User("login", "password", "subject", "recipients", "message", "header")
    user.send()
    user.recieve()