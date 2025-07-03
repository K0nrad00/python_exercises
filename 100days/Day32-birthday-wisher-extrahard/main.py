##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
import smtplib
import datetime as dt
import pandas
import random

my_email = "" #your email here
password = "" # Password for 3rd party apps here
EMAIL_BODY = "" #to change [NAME] in the letter

# 2. Check if today matches a birthday in the birthdays.csv
current_month , current_day = dt.datetime.now().month, dt.datetime.now().day
# print(current_day) # DEBUG

data = pandas.read_csv("birthdays.csv")
list_of_rows = data.to_dict(orient="records")
# print(list_of_rows) # DEBUG
# 3. If step 2 is true, pick a random letter from letter templates and replace the
# [NAME] with the person's actual name from birthdays.csv
letters = ["letter_templates/letter_1.txt" , "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
random_letter = random.choice(letters)

def change_name(selected_letter, name, senders_name):
    global EMAIL_BODY
    with open(selected_letter) as f:
        contents = f.read()
        EMAIL_BODY = contents.replace("[NAME]", name)
        EMAIL_BODY = EMAIL_BODY.replace("Senders_name", senders_name)

# 4. Send the letter generated in step 3 to that person's email address.
def send_email(birthday_email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_email,
                            msg=f"Subject:Happy Birthday\n\n{EMAIL_BODY}")

for row in list_of_rows:
    if current_month == row["month"] and current_day == row["day"]:
        change_name(random_letter, row["name"], senders_name="your_name_here") #your name
        send_email(row["email"])
