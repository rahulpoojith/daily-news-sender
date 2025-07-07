import time
import yagmail
import pandas
from news import NewsFeed
import datetime


def send_email():
    today=datetime.datetime.now()
    news_feed= NewsFeed(interest=row['interest'],from_date=(today - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),to_date=today.strftime("%Y-%m-%d"))
    email = yagmail.SMTP(user="pythonprocourse1@gmail.com", password="python_pro_course_1")
    email.send(to=row['email'],subject=f"Your{row[interest]} news for {today.strftime('%Y-%m-%d')}",
               contents=[f"Here is your news for {today.strftime('%Y-%m-%d')}",
                         news_feed.get_news()])
    
while True:
    if datetime.datetime.now().hour==17 and datetime.datetime.now().minute==51:
        df = pandas.read_excel("people.xlsx")

        for index, row in df.iterrows():
            if row['email'] != 'email':
                interest = row['interest']
                send_email()
    time.sleep(60)
