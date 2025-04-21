import os
import requests
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ["STOCK_KEY"]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

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
