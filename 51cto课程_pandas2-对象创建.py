#首先当然是导入我们需要的包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline #用以使创建的图形可以直接在网页中显示出来
#为了更好看，我们选择ggplot样式
import matplotlib
matplotlib.style.use('ggplot')

def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")
    
#对象创建
#创建一个Series
s  = pd.Series([1,3,5,np.nan,6,8]) #np.nan表示缺省对象
print(s)
make_end_line()

n1 = np.array(list("ABCDEFG"))
print(n1)
make_end_line()

s2 = pd.Series(n1)
print(s2)
make_end_line()

lis = list("ABCDEFG")
s3 = pd.Series(lis)
print(s3)
make_end_line()

s4 = pd.Series(list("ABCDEFG"),index=[11,21,31,41,51,61,71]) #指定每一项的索引 
print(s4)
print(s4[11])
make_end_line()

#DaraFrame (有点类似数据库里面的表table)
dates = pd.date_range("20160412", periods = 6) #以2016年04月12日为起始时间，
                                               #时间长度为6，（默认间隔是天）
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = list("ABCD")) #传入的数据是一个6x4的数组，索引是上方的dates，字段名是ABCD
print(df)
make_end_line()

df2 = pd.DataFrame({"A":1,
                    "B":pd.Timestamp("20160412"),
                    "C":pd.Series(1,index=list(range(4)),dtype="float32"),
                    "D":np.array([3]*4,dtype="int32"),
                    "E":pd.Categorical(["text","train","text","train"]),
                    "F":"foo"}) #通过字典方式表示DataFrame
print(df2)
make_end_line()
#以下为df2的显示
"""
   A          B    C  D      E    F
0  1 2016-04-12  1.0  3   text  foo
1  1 2016-04-12  1.0  3  train  foo
2  1 2016-04-12  1.0  3   text  foo
3  1 2016-04-12  1.0  3  train  foo

"""
print(df2.dtypes) #查看数据类型
#技巧：比如：输入完df2.后按下TAB键，可查看df2的字段和使用方法

