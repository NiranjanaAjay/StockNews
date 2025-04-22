import os
import requests
from dotenv import load_dotenv
from newsapi import NewsApiClient
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ["STOCK_KEY"]

NEWS_API_KEY = os.environ["NEWS_KEY"]
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

parameters ={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
response.raise_for_status()
stock_data = response.json()

daily_stock = stock_data["Time Series (Daily)"]
dates = list(daily_stock.keys())

yesterday_closing = float(daily_stock[dates[1]]["4. close"])
day_before_closing = float(daily_stock[dates[2]]["4. close"])

percentage_change = round((abs(yesterday_closing - day_before_closing)/day_before_closing)*100, 1)

if percentage_change>=5:
    if yesterday_closing > day_before_closing:
        MESSAGE = f"{STOCK}% : 🔺{percentage_change}\n"
    else:
        MESSAGE = f"{STOCK}% : 🔻{percentage_change}\n"
    client.messages.create(
        body=MESSAGE,
        from_="+17542871306",
        to=os.environ["PHONE_NUM"],
    )

    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                              category='business',
                                              language='en',
                                              country='us')
    for i in range(2):
        headline = top_headlines['articles'][i]['title']
        brief = top_headlines['articles'][i]['description']

        MESSAGE = f"Headline: {headline}\nBrief: {brief}"
        client.messages.create(
            body=MESSAGE,
            from_="+17542871306",
            to=os.environ["PHONE_NUM"],
        )



