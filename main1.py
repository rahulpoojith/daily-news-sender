import time
import yagmail
import pandas
import datetime
from news import NewsFeed


def send_email(row):
    today = datetime.datetime.now()
    news_feed = NewsFeed(
        interest=row['interest'],
        from_date=(today - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
        to_date=today.strftime("%Y-%m-%d")
    )

    email = yagmail.SMTP(user="pythonprocourse1@gmail.com", password="python_pro_course_1")
    email.send(
        to=row['email'],
        subject=f"Your {row['interest']} news for {today.strftime('%Y-%m-%d')}",
        contents=[
            f"Here is your news for {today.strftime('%Y-%m-%d')}",
            news_feed.get()
        ]
    )


# Main loop
while True:
    now = datetime.datetime.now()
    if now.hour == 17 and now.minute == 51:
        df = pandas.read_excel("people.xlsx")

        for index, row in df.iterrows():
            if row['email'] != 'email':  # skip header row if needed
                send_email(row)

        time.sleep(60)  # avoid sending again in the same minute
    else:
        time.sleep(30)