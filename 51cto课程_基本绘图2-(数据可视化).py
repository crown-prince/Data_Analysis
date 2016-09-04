import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


"""pd.set_option("display.notebook_repr_html",False) 以文本方式展示"""
"""pd.set_option("display.max_columns",6) 最大列表名 """
"""pd.set_option("display.max_rows",15) 最大行数 """
"""pd.set_option("display.width",78) 最大宽度"""
"""pd.set_option("precision",4) 展示的精度"""

def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")

"""绘制Series"""
ts = pd.Series(np.random.randn(1000), index = pd.date_range("20160414", periods = 1000))
print(ts.head())
make_end_line()
ts = ts.cumsum() #将数据累加，以体现趋势
plt.show(ts.plot(figsize = (20,8)))

"""如果索引包含日期，
plot就会调用gcf().autofmt_xdate试图将x轴格式化成更友好的方式"""

"""绘制DataFrame"""
df = pd.DataFrame(np.random.randn(1000,4),
                  index=pd.date_range("20160401",periods=1000),
                 columns=["A","B","C","D"])
print(df.head(10))
df = df.cumsum()
plt.show(df.plot())

#通过x，y关键字参数指定plot的x，y轴
df3 = pd.DataFrame(np.random.randn(1000,2),columns=["B","C"])
df3 = df3.cumsum()

df3["A"] = pd.Series(list(range(len(df))))
print(df3["A"])
plt.show(df3.plot(x="A",y="B")) #A作为x轴，B作为Y轴

