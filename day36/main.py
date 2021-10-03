import requests
import datetime
import os
from twilio.rest import Client

stocks = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']
company_name = {'AAPL': 'Apple Inc',
                'MSFT': 'Microsoft Inc',
                'GOOG': 'Google Inc',
                'AMZN': 'Amazon Inc',
                'TSLA': 'Tesla Inc'}

ALPHA_API = 'O6QVQ86CKL9UMKUM'
NEWS_API = '9a6e4f3235294d689c3bcac786ebb5ea'


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def date_list():
    now = datetime.datetime.today().date()
    two_day_list = []
    for i in range(1, 3):
        yesterday = now - datetime.timedelta(days=i)
        two_day_list.append(yesterday)
    return two_day_list


def stock_perc_change(stock):
    stock_param = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': stock,
        'apikey': ALPHA_API
    }
    stock_json = requests.get(url='https://www.alphavantage.co/query', params=stock_param)
    stock_json.raise_for_status()
    stock_data_full = stock_json.json()['Time Series (Daily)']
    # print(stock_data_full)
    day_list = date_list()

    # print(stock)
    stock_closings = [float(stock_data_full[str(item)]['4. close']) for item in day_list]
    # print(stock_closings)
    stock_percentage_change = round(((stock_closings[0] - stock_closings[1]) / stock_closings[0]) * 100,2)
    # print(stock_percentage_change)
    if stock_percentage_change >= 0:
        stock_perc_msg = f"\n✅ {stock_percentage_change}"
    else:
        stock_perc_msg = f"\n🔻 {-1 * stock_percentage_change}"
    # print(stock_perc_msg)

    if stock_percentage_change < -0.5 or stock_percentage_change > 0.5:
        return [True, stock_perc_msg]
    else:
        return [False, 'No news']


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def stock_news(s_news):
    news_param = {
        'q': company_name[s_news],
        'apiKey': NEWS_API,
        'qInTitle': 'Stock',
        'from': date_list()[0],
        'language': 'en',
        'sortBy': 'relevancy',
    }

    news_json = requests.get(url='https://newsapi.org/v2/everything', params=news_param)
    try:
        news = news_json.json()['articles'][0]
        full_news = f"Headline: {news['title']}\nContent: {news['content'][:200]}...\nLink:{news['url']}\n\n"
    except IndexError:
        full_news = f"No news on {news_param['q']}"
    return full_news


final_full_msg = ''
for stk in stocks:
    stock_status = stock_perc_change(stk)
    if stock_status[0]:
        news_status = stock_news(stk)
        final_ind_news = f'{stk} : {stock_status[1]}\n{news_status}'
        final_full_msg += final_ind_news

        account_sid = 'AC229886e1b6d27258f49a032d5d1a99fa'
        auth_token = '03a12a7328890f7a3274fbc059d04f85'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=final_ind_news,
                from_='+16194942596',
                to='+918983517226'
        )
        print(message.status)

print(final_full_msg,len(final_full_msg))

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# account_sid = 'AC229886e1b6d27258f49a032d5d1a99fa'
# auth_token = '03a12a7328890f7a3274fbc059d04f85'
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#     .create(
#         body=final_full_msg,
#         from_='+16194942596',
#         to='+918983517226'
#     )
# print(message.status)
