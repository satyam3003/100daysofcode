# import smtplib
#
# my_email = 'satyam30032001@gmail.com'
# password = 'Baldawa@30'
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password='Baldawa@30')
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='baldawasatyam30@gmail.com',
#                         msg='Subject:Python Mail \n\nHello to me from me! Glad to meet me as me')  # Subject:--- to add subject ---- \n\n to indicate subject is over and further add content

import smtplib
import datetime
import random

my_email = 'satyam30032001@gmail.com'
password = 'Baldawa@30'
now = datetime.datetime.now()
day = now.weekday()
if day == 2:
    with open('day32/quotes.txt') as qt:
        quotes = qt.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password='Baldawa@30')
        connection.sendmail(from_addr=my_email,
                            to_addrs='baldawasatyam30@gmail.com, satyam.baldawa@walchandsangli.ac.in',
                            msg=f'Subject:Half way through the week motivation \n\n{quote}')
