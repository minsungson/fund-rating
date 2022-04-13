from locale import currency
import yfinance as yf
import os
from datetime import datetime, timedelta
import colorama
import pandas as pd
from colorama import Fore, Back
colorama.init(autoreset=True)

startDate = datetime.today()
endDate = startDate + \
    timedelta(days=7)

def stockInfo():
    os.system("clear")
    print("" + Back.WHITE + Fore.BLACK + " Basic Information about " + ticker.info["shortName"] + " \n")
    # print("Sector: " + Fore.YELLOW + ticker.info["sector"])
    if "sector" in ticker.info:
        print("Sector: " + Fore.YELLOW + ticker.info["sector"])
    else:
        print("Sector" + Fore.RED + "N/A")
    if "country" in ticker.info:
        print("Country: " + Fore.YELLOW + ticker.info["country"])
    else:
        print("Country" + Fore.RED + "N/A")
    if "exchangeTimezoneName" in ticker.info:
        print("Trading Time Zone: " + Fore.YELLOW + ticker.info["exchangeTimezoneName"])
    else:
        print("Trading Time Zone " + Fore.RED + "N/A")
    if "financialCurrency" in ticker.info:
        print("Trading Currency: " + Fore.YELLOW + ticker.info["financialCurrency"])
    else:
        print("Trading Currrency: " + Fore.RED + "/A")
    if "isin" in ticker.info:
        print("ISIN: " + Fore.YELLOW + ticker.info["isin"])
    else:
        print("ISIN: " + Fore.RED + "N/A")
    if "major_shareholders" in ticker.info:
        print("Major Shareholders: " + Fore.YELLOW + ticker.info["major_shareholders"])
    else:
        print("Major Shareholders: " + Fore.RED + "N/A")
    if "institutional_holders" in ticker.info:
        print("Institutional Holders:" + Fore.YELLOW + ticker.info["institutional_holders"])
    else:
        print("Institutional Holders: " + Fore.RED + "N/A")
    if "dividend" in ticker.info:
        print("Latest Dividend Payment: " + Fore.YELLOW + ticker.info["dividend"])
    else:
        print("Latest Dividend Payment: " + Fore.RED + "N/A")

    cont()

def financialData():
    print("" + Back.WHITE + Fore.BLACK + " Financial Information about " + ticker.info["shortName"] + " \n")
    global rawData
    # rawData = ticker.history(period="7d")
    print(rawData[["Open"]])
    cont()

# # def calculation():
# #     df = pd.DataFrame(rawData)
# #     list = df['Open'].values.tolist()
# #     # sigma = rawData.sum()
# #     # print("Σ open =", sigma)
# #     # print("     x̄ =", sigma/7)
# #     print(type(rawData))

def cont():
    input("\nPress [ENTER] to continue ")
    os.system("clear")

def run():
    os.system("clear")
    global symbol, ticker
    # symbol = input("Enter the ticker you would like a rating of: ")
    symbol = "GOOGL" # set static for debugging
    ticker = yf.Ticker(symbol)
    stockInfo()
    # financialData()
    # calculation()

run()

# ticker = yf.Ticker("GOOGL")
# print(ticker.isin)