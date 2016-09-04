# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import lxml

def get_data():
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0",}
    url = "http://www.open-open.com/github/view/github2016-09-03.html"
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respHtml = (resp.read()).decode("utf-8")
    #print(respHtml)
    soup = BeautifulSoup(respHtml, "lxml")
    summary = soup.find("div", {"class":"main_right_body"})
    tables = summary.find_all("table")
    print(tables)    
def main():
    get_data()

if __name__ == "__main__":
    main()
