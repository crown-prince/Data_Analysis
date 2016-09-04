import pandas as pd
import numpy as np

def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")
    
dates = pd.date_range("20160412", periods = 6) #以2016年04月12日为起始时间，
                                               #时间长度为6，（默认间隔是天）
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = list("ABCD")) #传入的数据是一个6x4的数组，索引是上方的dates，字段名是ABCD
print(df) #查看所有数据
make_end_line()
print(df.head(2)) #不带参数时默认查看前5行，带参数时，查看指定行数
make_end_line()
print(df.tail(2)) #不带参数时默认查看倒数5行，带参数时，查看倒数指定行数
make_end_line()
print(df.index) #查看索引值
print(df.columns) #查看字段名
make_end_line()
print(df.values) #查看DataFrame的值
make_end_line()
print(df.describe()) #查看数据的一些简单统计结果
                     #计算各个列的基本描述统计值，包含计数，平均数，标准差，最大值，最小值及4分位差（四分位差主要用于测度顺序数据的离散程度）
make_end_line()
print(df.T) #将索引变为字段，将字段变为索引
make_end_line()
#按值排序
print(df.sort_values(by="A")) #根据A字段进行排序
print(df.sort_values(by="B")) #根据B字段进行排序



