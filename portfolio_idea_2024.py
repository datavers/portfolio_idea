import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf 

tickers = yf.Tickers('xle xlb xli')
print(tickers)