import pandas as pd
import numpy as np

def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")
def f1(x):
    return x + 10

dates = pd.date_range("20160412", periods = 6) #以2016年04月12日为起始时间，
                                               #时间长度为6，（默认间隔是天）
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = list("ABCD")) #传入的数据是一个6x4的数组，索引是上方的dates，字段名是ABCD
print(df) #查看所有数据
make_end_line()
print(df.apply(f1)) #通过f1函数，即将DataFrame中每个值加10
print(df.apply(lambda x:x.max()- x.min())) #lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义


