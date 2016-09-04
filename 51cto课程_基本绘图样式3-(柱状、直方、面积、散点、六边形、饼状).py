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

#绘制柱状图
df2 = pd.DataFrame(np.random.randn(10,4),columns=list("ABCD"))
plt.show(df2.plot(kind = "bar")) #方法1
plt.show(df2.plot.bar()) #方法2
plt.show(df2.plot.bar(stacked = True)) #将数据堆积起来
plt.show(df2.plot.barh()) #也可以通过barh将数据横向展示

#绘制直方图
df3 = pd.DataFrame({"a":np.random.randn(1000) + 1,
                    "b":np.random.randn(1000),
                    "c":np.random.randn(1000) - 1},
                    columns=["a","b","c"])

plt.show(df3.plot.hist(alpha=0.5))
#alpha 指定透明度
plt.show(df3.plot.hist(stacked=True,bins=20)) #使用stacked=True表示堆积，bins指定格子(bin)数量
plt.show(df3.plot.hist(orientation="horizontal",bins=20))
df3.hist(color="b",alpha=0.5,bins=20)
plt.show() #将结果通过多个子图展示

#绘制面积图
#通过Series.plot.area()或者DataFrame.plot.area()创建,默认stacked，
#如果要生成stacked面积图，每个字段必须都为正数或者所有非负数。
#当输入的数据包括NaN时，会自动用0填充，如果需要删除或者填充这些值，可以在绘图前调用DataFrame.dropna()或者DataFrame.fillna
df = pd.DataFrame(np.random.rand(10,4),columns=list("abcd")) #注意这里用的是np.random.rand 而不是.randn
plt.show(df.plot.area())
plt.show(df.plot.area(stacked=False))#指定stacked=False,使其不堆积

#绘制散点图(点状图)
df = pd.DataFrame(np.random.rand(50,4),columns=list("abcd"))
plt.show(df.plot.scatter(x="a",y="b"))

ax = df.plot.scatter(x="a",y="b",color="DarkBlue",label="Group 1") #指定多个字段组在一个图中，可以指定ax重复plot方法，
df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax) #推荐指定颜色以及标签用以区别不同的组
plt.show()

plt.show(df.plot.scatter(x="a",y="b",c="c",s=120)) #通过c关键词参数指定色度条，s关键字参数指定点的大小
                                                   #注：传入的c,s对象都可以是等长的序列

plt.show(df.plot.scatter(x='a', y='b', s=df['c']*200))

#绘制六边形图
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df['b'] = df['b'] + np.arange(1000)
plt.show(df.plot.hexbin(x="a",y="b",gridsize=25))

#绘制饼状图
#如果数据包含NaN，它会自动用0填充，负值则会报ValueError
series = pd.Series(np.random.rand(4),index=list("ABCD"),name="Series")
print(series)
series.plot.pie()
plt.savefig("text.png") #保存图形

#如上的方法，默认是有所收缩的，需要通过指定一样的长宽（制成正方形）或者强制调用ax.set_aspect('equal')
plt.show(series.plot.pie(figsize=(6,6)))
plt.show(series.plot.pie(labels=['AA', 'BB', 'CC', 'DD'], colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6)))
#labels：标签，fontsize=20：字体大小，autopct：比例的精度

#如果传入的值总和小于1，会绘制一个扇形
series = pd.Series([0.1] * 4, index=['a', 'b', 'c', 'd'], name='series2')
plt.show(series.plot.pie(figsize=(6, 6)))

#注意DataFrame需要指定关键字参数y=，或者subplot=True
df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
df.plot.pie(subplots=True, figsize=(8, 4))
plt.show()
#还可以指定标签，字体大小等

