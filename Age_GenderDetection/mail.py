import os
import smtplib
from smtplib import SMTP
from typing import Union,Any

Email_Adress: Union[str, Any] = os.environment.get*("Email_User")
Email_Password = os.environment.get*("Email_Pass")

smtp: SMTP
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    server.starttls()
    smtp.eclo()

    smtp.login('theftdetection1234@gmail.com','theft@123')
    body = "How about your dinner at 6 pm this saturday ?"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail('varadkulkarni3112@gmail.com','Mail sent from Me')

print('Mail sent')