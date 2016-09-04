import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")

ts = pd.Series(np.random.randn(1000), index = pd.date_range("20160414", periods = 1000))
print(ts.head())
make_end_line()
ts.plot(figsize = (12, 8))  #figsize：用以设置绘出的图的大小
plt.show()
ts = ts.cumsum() #将数据累加，以体现趋势
plt.show(ts.plot())
"""cumsum()直观举例"""
ts2 = ts[:10]
print(ts2)
print(ts2.cumsum())
make_end_line()

#plot通过标签很容易绘出所有字段(多条曲线在一个图里)
df = pd.DataFrame(np.random.randn(1000,4),
                  index=pd.date_range("20160401",periods=1000),
                 columns=["A","B","C","D"])
print(df.head(10))
df = df.cumsum()
plt.show(df.plot())
