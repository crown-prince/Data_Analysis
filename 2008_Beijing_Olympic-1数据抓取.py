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

def main():
    url = "http://baike.baidu.com/view/16667.htm"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0",}
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req, timeout=10) #data=urllib.request.urlopen(url).read()  
    respHtml = (resp.read()).decode("utf-8")
    #print(respHtml)
    soup = BeautifulSoup(respHtml, "lxml")
    summary = soup.find("div", {"class":"main-content"})
    tables = summary.find_all("table")
    #print(len(tables))

    """for i in range(len(tables)):
        ths = tables[i].findAll("th")
        for j in ths:
            if u"名次" in j.text:
                print(i) """
    data = []
    columns_list = []
   
    rows = tables[14].findAll("tr")
    ths = tables[14].findAll("th") #<th>名次&#12288;</th>

    for cols in ths:
        #print(cols.text)
        columns_list.append(cols.text)
    for tr in rows:
        cols = tr.findAll("td")
        for td in cols:
            text = td.find(text = True)
            #print(text)
            data.append(text)
    
    for i in range(len(columns_list)):
        columns_list[i] = ''.join(columns_list[i].split('\n'))
    columns_list[0] = ''.join(columns_list[0].split('\u3000'))
    #print(data)
    
    with open("2008.csv", "w", newline="") as datacsv: #参数newline是用来控制文本模式之下，一行的结束字符。可以是None，’’，\n，\r，\r\n等
        csvwriter = csv.writer(datacsv,dialect = ("excel"))
        csvwriter.writerow(columns_list)
        i = 0
        while i < (len(data) - 5): #循环以插入多行
            put = []
            for j in range(i, i + 6):
                put.append(data[j])
                #print(j)
            csvwriter.writerow(put)
            i = i + 6
            
    datacsv.close() 
if __name__ == "__main__":
    main()
