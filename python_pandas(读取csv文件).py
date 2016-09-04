import pandas as pd
import matplotlib.pyplot as plt

# Reading data locally
#df = pd.read_csv('/Users/al-ahmadgaidasaad/Documents/d.csv')

# Reading data from web
data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
df = pd.read_csv(data_url)

print(df)
print(df.describe())
plt.show(df.plot(kind = 'box')) 
"""
pd.options.display.mpl_style = 'default' # Sets the plotting display theme to ggplot2
df.plot(kind = 'box')
"""
