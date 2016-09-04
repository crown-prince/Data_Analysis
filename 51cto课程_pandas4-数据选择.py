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

"""直接通过字段访问"""
print(df["A"]) #方法1
print(df.A) #方法2
#通过索引切片访问
make_end_line()
print(df[0:2])
make_end_line()
#通过索引值
print(df["20160412":"20160414"])
make_end_line()

"""通过标签（索引）访问"""
print(df.index) #先通过df.index查看索引
print(df.loc["2016-04-12"]) #显示该索引对应的数据
make_end_line()
print(df.loc[:]) #显示所有值
print(df.loc[:, ["A", "C"]]) #显示所有索引的A、C字段
make_end_line()
print(df.loc["20160412":"20160414",["A","B"]]) #这里将包括终点（与列表不同）
make_end_line()

"""通过位置访问"""
print(df.iloc[3])
print(df.iloc[3:5,0:4:2])
#行(row)切片
print(df.iloc[1:3,:])
make_end_line()
#获取值
print(df.iloc[1,1])
#获取值的速度更快方式
print(df.iat[1,1])
make_end_line()

"""布尔索引"""
print(df)
#df[df.A > 0]
print(df[df.B > 1]) #输出B > 1的行
make_end_line()
print(df[df > 0]) #where条件运算，显示df中大于0的值，不满足的将用NaN代替
make_end_line()
df3 = df[df > -2]
print(df3.dropna()) #再取出DataFrame中的NaN

"""使用isin方法过滤"""
df2 = df.copy() #将df复制一份至df2

df2["E"] = ["1","1","2","3","4","3"]
print(df2)
print(df2[df2["E"].isin(["2","4"])]) #提取出有2, 4内容的部分


