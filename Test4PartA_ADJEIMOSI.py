#A.Import the necessary libraries and read the ‘csv” data. 

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


stock = pd.read_csv('stock3.csv')




#In order to perform a graphical comparison between GOOG and AAPL, plot closing values for both GOOG and AAPL

#plotting closing values graphics for GOOG
plt.plot(stock['GOOG'], color = 'black')
plt.title("Graphical comparison for closing values of GOOG")
plt.show

#plotting closing values graphics for AAPL
plt.plot(stock['AAPL'])
plt.title("Graphical comparison for closing values of AAPL")
plt.show()



#Calculate the simple daily percentage changes for four stocks. The simple daily percentage change (without dividends and other factors) is the percentage change in the value of a stock over a single day of trading. It is defined by the following formula:

stock['daily_GOOG_price_change']=stock['GOOG']/stock['GOOG'].shift(1) -1
print("\n---Simple Daily Percentage change for GOOG---" )
print(stock['daily_GOOG_price_change'].head(7))
#Calculate the daily percentage changes for AAPL
stock['daily_AAPL_price_change']=stock['AAPL']/stock['AAPL'].shift(1) -1
print("\n---Simple Daily Percentage change for AAPL---" )
print(stock['daily_AAPL_price_change'].head(7))
#Calculate the daily percentage changes for EBAY
stock['daily_EBAY_price_change']=stock['EBAY']/stock['EBAY'].shift(1) -1
print("\n---Simple Daily Percentage change for EBAY---" )
print(stock['daily_EBAY_price_change'].head(7))
#Calculate the daily percentage changes for CVS
stock['daily_CVS_price_change']=stock['CVS']/stock['CVS'].shift(1) -1
print("\n---Simple Daily Percentage change for CVS---" )
print(stock['daily_CVS_price_change'].head(7))


#Analyzing the distribution of returns for AAPL and GOOG
#Plot Histogram of GOOG
stock['daily_GOOG_price_change'].hist(color = 'skyblue')
plt.title("Distributions of Returns for GOOG")
plt.show()
#Plot Histogram of AAPL
stock['daily_AAPL_price_change'].hist(color = 'purple')
plt.title("Distributions of Returns for AAPL")
plt.show()
#The daily % for GOOG has a normal distribution, AAPL is does not have a normal distribution because it is skewed to the right.




#Compare the average daily changes between GOOG and AAPL using a scatter plot
#Display a scatter plot for the GOOG and AAPL average daily change
stock.plot(x = 'daily_GOOG_price_change', y = 'daily_AAPL_price_change', kind= 'scatter', color= 'green')
plt.title("Average Daily changes between GOOG and AAPL")
plt.show()
#The scatter shows a minor correlation. The closer it is to the center the better correlation it has.



#Examine the correlation of the stocks based on the closing price, and visualize the correlation matrix using a heat map
#Display the heat map to view corellation between closing price of stocks
corr = stock.corr()
plt.imshow(corr, cmap = 'cool', interpolation = 'none')
plt.colorbar()
plt.title("Examination of the correlation of the stocks based on closing price using a Heat Map")
plt.show()
#Based on the heat map there seems to be no sort of correlation. 


