##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import smtplib
import random

# ----------------- email and password ----------
my_email = 'satyam30032001@gmail.com'
password = 'Baldawa@30'


# ----------- Setting up pandas -----------------
data = pd.read_csv('birthday_wisher/birthdays.csv')  # day32/birthday_wisher/birthdays.csv
record_list = data.to_dict('records')


# ------------ Setting up day and month ----------
now = dt.datetime.now()
month = now.month
day = now.day


# ----------------- choosing the message/letter ------------
letters = ['letter_1', 'letter_2', 'letter_3']
letter = random.choice(letters)
letter_today = f'birthday_wisher/letter_templates/{letter}.txt'  #day32/birthday_wisher/letter_templates/{letter}.txt

with open(letter_today) as lt:
    letter_message = lt.read()
    letter_message = letter_message.replace('Angela', 'Satyam')


# ------------- Checking if record match -------------
for record in record_list:
    if record['month'] == month and record['day'] == day:
        letter_message = letter_message.replace('[NAME]', record['name'])
        print(letter_message)
        receiver = record['email']
        print(receiver)
        # ------------------ Sending the email ---------------
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=receiver,
                                msg=f'Subject:Satyam Baldawa wishes you a very happy birthday! \n\n{letter_message}\n~generated using python')
        print(f"Message send to {record['name']}")
