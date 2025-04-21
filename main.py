import os
import requests
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ["STOCK_KEY"]
NEWS_API_KEY = os.environ["NEWS_KEY"]

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


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

# parameters ={
#     "function":"TIME_SERIES_DAILY",
#     "symbol":STOCK,
#     "apikey": STOCK_API_KEY
# }
# response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
# response.raise_for_status()
# stock_data = response.json()
# print(stock_data)
#
# daily_stock = stock_data["Time Series (Daily)"]
# dates = list(daily_stock.keys())
#
# yesterday_closing = float(daily_stock[dates[1]]["4. close"])
# day_before_closing = float(daily_stock[dates[2]]["4. close"])
#
# percentage_change = round((abs(yesterday_closing - day_before_closing)/day_before_closing)*100, 1)*2
#
# if percentage_change>=5:
    headlines=[]
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                              category='business',
                                              language='en',
                                              country='us')
    for i in range(2):
        headline = top_headlines['articles'][i]['title']
        headlines.append(headline)



