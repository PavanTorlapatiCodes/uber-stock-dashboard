import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#download real uber stock data
print("downloading Uber Stock Data...")
data = yf.download('UBER', period='1mo')
#numpy mazic
data['Returns']=np.log(data['Close']/data['Close'].shift(1))*100 #daily%change
data['MA_5']=data['Close'].rolling(5).mean()   #5-day average
data.to_csv('uber_stock.csv')
print("✅ CSV saved!")
#charts with numpy data
plt.figure(figsize=(12,8))
plt.plot(data['Close'],label='price')
plt.plot(data['MA_5'],label='Numpy MA')
plt.title('Uber Stock + NumPy Analysis')
plt.legend()
plt.savefig('uber_chart.png')
plt.show()
#numpy states
mean_ret=np.mean(data['Returns'].dropna())
vol=np.std(data['Returns'].dropna())
print(f"Numpy States Mean Retturn{mean_ret:.2f}%),volatility {vol:.2f}%")
