# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import lxml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv
matplotlib.style.use('ggplot')

def main():
    df = pd.read_csv("2008-ten.csv")
    plt.show(df.plot()) #各项数据折线图
    plt.show(df.plot(x="Total number of MEDALS", y="Gold")) #金牌数和奖牌数的关系
    plt.show(df.plot(x="Total number of MEDALS", y="Silver")) #银牌数和奖牌数的关系
    s = pd.Series(df["Gold"]) #各国家金牌占比
    s.plot.pie()
    plt.show(s.plot.pie(autopct='%.2f', figsize=(6,6)))  
if __name__ == "__main__":
    main()
