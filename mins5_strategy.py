# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 08:45:03 2025

@author: Balachandar 
"""

#Import the requierd libraries 
from tvDatafeed import TvDatafeed, Interval
import requests
import os

#set environment variable
def set_environ():
    os.environ['TOKEN'] = '8380163368:AAHq78IVBsKUAenRc_mrDtd-tcGpun_D9kM'
    os.environ['CHAT_ID'] = '8451555149'
    
#get Forex data 
def get_forex_data():
    # TradingView login (guest mode works too)
    tv = TvDatafeed()
    # Fetch 15 mins of XAUUSD data
    df = tv.get_hist(symbol='XAUUSD', exchange='OANDA', interval=Interval.in_5_minute, n_bars=100).reset_index()
    df = df.reset_index(drop=True)
    # Define sessions in Mexico time
    return df

def mins5_strategy(data):
    last_open = data['open'].iloc[-1]
    last_close = data['close'].iloc[-1]
    diff = last_close - last_open
    print(diff)

    if diff >= 10:
        return f"Bullish candle: +{diff:.2f} points"
    elif diff <= -10:
        return f"Bearish candle: {diff:.2f} points"
    else:
        pass
    
def send_message(message,bot_token,chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
        }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)


if __name__ == '__main__':
    data = get_forex_data()  
    result = mins5_strategy(data)
    if result is not None:
        print('hello')
        set_environ()
        bot_token = os.getenv("TOKEN")
        chat_id = os.getenv("CHAT_ID")
        send_message(result,bot_token,chat_id)
    else:
        pass
        
    