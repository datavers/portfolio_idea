import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import requests
import certifi

response = requests.get('https://yahoo.com', verify=certifi.where())
print(response.content)

import yfinance as yf 

tickers = yf.Tickers('MSFT XLB XLI')
aapl = yf.Ticker('AAPL')
print(f"Ez egy szöveg")
print(tickers.tickers['MSFT'].history(period="1mo"))
print(aapl.info)