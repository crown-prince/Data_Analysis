#http://tushare.waditu.com
#TuShare是一个开源的python财经数据接口包 (也包括新闻、电影的数据)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import seaborn as sns
import tushare as tsh
sns.set_style("whitegrid")

pd.set_option("display.max_columns",15)
pd.set_option("display.max_rows",10)
pd.set_option("display.width",78)
pd.set_option("precision",15) #展示的精度

def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")

def main():
    #分别是招商银行，建设银行，上证指数, 浦发银行，民生银行
    stock_list = {"zsyh":"600036","jsyh":"601939","szzs":"000001","pfyh":"600000","msyh":"600061"}

    for stock, code in stock_list.items():
        globals()[stock] = tsh.get_hist_data(code,start="2015-01-01",end="2016-04-16")
        #code:股票代码，start:开始时间，end:结束时间
    #print(zsyh) #打印招商银行的股票信息
    make_end_line()
    print(zsyh.head())
    make_end_line()
    print(zsyh.columns)
    make_end_line()
    """
    字段说明

    date：日期
    open：开盘价
    high：最高价
    close：收盘价
    low：最低价
    volume：成交量
    price_change：价格变动
    p_change：涨跌幅
    ma5：5日均价
    ma10：10日均价
    ma20: 20日均价
    v_ma5: 5日均量
    v_ma10: 10日均量
    v_ma20: 20日均量
    turnover:换手率[注：指数无此项]
    """
    print(zsyh.describe())
    make_end_line()
    print(zsyh.info())
    make_end_line()
    plt.show(zsyh["close"].plot(figsize=(12,8))) #股票分析也一般是收盘价
    #pd.set_option("display.float_format", lambda x: "%10.3f" % x) 
    plt.show(zsyh["volume"].plot(figsize=(12,8)))
    zsyh[["close","ma5","ma10","ma20"]].plot(subplots = True)
    plt.show()
    plt.show(zsyh[["close","ma5","ma10","ma20"]].plot(figsize=(12,8),linewidth=2))
    plt.show(zsyh["p_change"].plot())
    plt.show(zsyh["p_change"].plot(figsize=(10,4),legend=True,linestyle="--",marker="o"))
    #改变线条和点的显示方式
    plt.show(zsyh["p_change"].hist(bins=20))
    plt.show(zsyh["p_change"].plot.kde()) #求出核密度
                                          #核密度估计(kernel density estimation)是在概率论中用来估计未知的密度函数
    plt.show(sns.kdeplot(zsyh["p_change"].dropna()))
    plt.show(sns.distplot(zsyh["p_change"].dropna())) #将直方图和核密度图放置在一个图形中，相互比较

def stock():
     #分别是招商银行，建设银行，上证指数, 浦发银行，民生银行
    stock_list = {"zsyh":"600036","jsyh":"601939","szzs":"000001","pfyh":"600000","msyh":"600061"}
    for stock, code in stock_list.items():
        globals()[stock] = tsh.get_hist_data(code,start="2015-01-01",end="2016-04-16")
    stock_list2 = stock_list.keys()
    #print(stock_list2)
    sl = [globals()[st]["close"] for st in stock_list2]
    df_close = pd.concat(sl,axis=1,join='inner')
    df_close.columns = stock_list2
    #print(df_close)
    df_close.sort_index(ascending=True,inplace=True) #ascending 参数用于控制升序或降序，默认为升序。
    pc_ret = df_close.pct_change() #这里单独写了相关的方法计算涨幅度
    print(pc_ret)
    make_end_line()
    print(pc_ret.mean())
    make_end_line()
    #建设银行与建设银行的关系
    plt.show(sns.jointplot("zsyh","jsyh",pc_ret,kind="hex")) #求解 皮尔逊相关系数，1表示变量完全正相关， 0表示无关， -1表示完全负相关。
    plt.show(sns.jointplot("zsyh","jsyh",pc_ret,kind="scatter"))
    plt.show(sns.jointplot("zsyh","szzs",pc_ret,kind="scatter"))
    plt.show(sns.pairplot(pc_ret[["jsyh","zsyh","pfyh","msyh"]].dropna())) #同时相互比较多组数据
    print(pc_ret.std()) #查看标准差，通过标准差，可以了解该股票的浮动，即是否稳定
    make_end_line()
    rets = pc_ret.dropna()
    print(rets.mean())
    make_end_line()
    area = np.pi *20 #点的大小
    plt.scatter(rets.mean(),rets.std())    #分别以rets的平均值，标准差为xy轴 
    plt.xlabel("Expected Return")#分别设定xy轴的标注
    plt.ylabel("Risk")
    for label,x,y in zip(rets.columns,rets.mean(),rets.std()):
        plt.annotate(
            label,
            xy = (x,y),xytext = (50,50),
            textcoords = "offset points",ha = "right",va = "bottom",
            arrowprops = dict(arrowstyle = "-",connectionstyle = "arc3,rad=-0.3"))
    plt.show()
if __name__ == "__main__":
    #main()
    stock()
     

