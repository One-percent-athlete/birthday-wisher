##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# birthday wisher code
import datetime as dt
import random
import smtplib
import pandas as pd
import dotenv
import os 
dotenv.load_dotenv()                    
my_email = os.environ.get('my_email')
password = os.environ.get('password')


my_email = my_email
password = password
now = dt.datetime.now()
today = (now.month, now.day)

df = pd.read_csv('birthdays.csv')
birthday_dict = {(row["month"], row["day"]):row for (index,row) in df.iterrows()}

number = random.randint(1,3)

if today in birthday_dict:
    file_path = f"letter_templates/letter_{number}.txt"

    with open(file_path) as f:
        data = f.read()
    new_data = data.replace("[NAME]", birthday_dict[today]["name"])
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            # to_addrs=birthday_dict[today]["email"]
            to_addrs=my_email, 
            msg=f"Subject:Happy Birthday\n\n{new_data}")



# weekday quote code 
# import smtplib
# import datetime as dt
# import random

# my_email = "ryu.super.s@gmail.com"
# password = "poqhmrownbdgvdjf"
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 4:
#     with open("quotes.txt") as file:
#         quotes = file.readlines()
#         quote= random.choice(quotes)

#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs=my_email, 
#             msg=f"Subject:Daily quotes\n\n{quote}")


