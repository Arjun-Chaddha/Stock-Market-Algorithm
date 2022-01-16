from TurningPoint import getPoints
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import math

stocks = ['ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJFINANCE.NS', 'BAJAJFINSV.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GAIL.NS', 'GRASIM.NS', 'HDFC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'IOC.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SHREECEM.NS', 'SUNPHARMA.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS', 'LT.NS', 'TECHM.NS', 'HCLTECH.NS']

import datetime

gains = []


def function(stock):
    data, highs, lows = getPoints(stock, R_=1.05, alpha=1, beta=100, combined=False, showPlot=False,
                                  getData=True, startDate='2019-01-01', endDate='2022-01-01')

    # plt.plot(data["close"], '-o', markevery=highs + lows, markersize=5, fillstyle='none')
    # plt.show()

    buy = []
    # print (lows)
    sell = []

    for i in range(0, len(lows)):
        if data['close'][lows[i - 1]] < data['close'][lows[i - 2]]:
            if data['close'][lows[i]] > data['close'][lows[i - 1]]:
                buy.append(lows[i])

    for j in range(0, len(highs)):
        if data['close'][highs[j - 1]] > data['close'][highs[j - 2]]:
            if data['close'][highs[j]] < data['close'][highs[j - 1]]:
                sell.append(highs[j])

    # print (buy)
    # print (sell)

    plt.plot(data["close"], '-o', markevery=buy, markersize=5)
    plt.plot(data["close"], '-o', markevery=sell, markersize=5)
    plt.title(stock)
    # plt.show()

    # if not math.isnan(buy[-1]):
    #     print (stock)

    money = 0
    number_of_stocks = 0
    investment = 0
    invests = []

    a = 0
    while a < len(data):
        if a in buy:
            money = money - (data['close'][a])
            number_of_stocks += 1
            invests.append(money)

        if a in sell:
            money = money + (data['close'][a] * number_of_stocks)
            number_of_stocks = 0
            invests.append(money)

        a += 1

    if number_of_stocks > 0:
        money = money + (number_of_stocks * data['close'][-1])
        number_of_stocks = 0

    investment = abs(min(invests))
    percentage_change = money * 100 / investment

    print(percentage_change)

    # print (len(stocks))

    return percentage_change, stock


for stock in stocks:
    gain = function(stock)[0]
    gains.append(gain)


print(gains)
print (np.mean(gains))
