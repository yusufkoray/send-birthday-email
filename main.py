import pandas as pd
import smtplib
import datetime
import glob
import random
import os

my_mail="ykcspor@gmail.com"
to_mail="yusufkoraycan@yahoo.com"
password = os.getenv("EMAIL_PASSWORD")

birthday=pd.read_csv("birthdays.csv")
name=birthday["name"][0]
month=birthday["month"][0]
day=birthday["day"][0]

today=datetime.datetime.now()
today_month=today.month
today_day=today.day
def letter_process():
    folder_path="letter_templates"
    txt_files=glob.glob(f"{folder_path}/*.txt")
    random_txt_name=random.choice(txt_files)
    with open(f"{random_txt_name}","r") as file:
        content=file.readlines()
        content[0]=content[0].replace('[NAME]',name)
    return "".join(content)

if today_month == month and today_day == day:
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=my_mail,password=password)
    connection.sendmail(from_addr=my_mail,to_addrs=to_mail,msg=letter_process())
    connection.close()
else:
    pass