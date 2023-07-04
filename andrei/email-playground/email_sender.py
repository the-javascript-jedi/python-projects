import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

#  for temporary password using google account use below link
# https://myaccount.google.com/apppasswords

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='NS'
email['to']='nithinsam77@gmail.com'
email['subject']="You won 10000000 dollars"

# email.set_content('i am a Python Master')
# substitute the variable in index.html and change to new value
email.set_content(html.substitute({'name':'tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@gmail.com','password')
    smtp.send_message(email)
    print('all good boss!')

    # python email_sender.py