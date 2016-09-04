#大多数plot方法拥有一套关键字参数用以控制返回图形的布局与样式
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

#线条样式：
ts = pd.Series(np.random.randn(1000),index=pd.date_range("20160412",periods=1000))
ts = ts.cumsum()
plt.show(ts.plot(style="k^",label="Series",figsize=(12,8))) #style参数,用以控制图像的线条样式
                                                  #可通过http://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D 查阅

#控制刻印文字(表示线条的文字)：
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.show(df.plot())
plt.show(df.plot(legend=False)) #legend=False,用以去除刻印文字


#对数据的掌控：
###如下，因为我们将数值给exp指数求值，所以下面的图不会太优雅
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = np.exp(ts.cumsum())
plt.show(ts.plot())
#当我们将y轴通过log指数缩放就相对而言要直观一些
plt.show(ts.plot(logy=True))

#建立第二个Y轴
df.A.plot()
plt.show(df.B.plot(secondary_y=True, style='g'))

#将多个曲线分别绘制在一张图中
df.plot(subplots=True,figsize=(6,6))
plt.show() 

#使用布局(layout) (绘制多个图像)
#通过layout关键字参数指定布局，它接受一个layout = (行数，列数) 的元组
df.plot(subplots=True,layout=(2,3),figsize=(18,6),sharex=False) #通过sharex指定是否共享x轴
plt.show() 


#额外绘制数据表格
df = pd.DataFrame(np.random.rand(5,3),columns=["A","B","C"])
plt.show(df.plot(table=True))

#隐藏x轴（比如这里为了让表格和x轴互不影响，隐藏了x轴）
fig, ax = plt.subplots(1, 1)
df = pd.DataFrame(np.random.rand(5,3),columns=["A","B","C"])
ax.get_xaxis().set_visible(False)
plt.show(df.plot(table=True,ax=ax))

#选择色谱：
#当需要绘制大量的数据序列的时候，需要不同的颜色用以区分，由于默认的颜色可能会
#有重复，所以可以使用colormap关键字参数，来绘制一系列的不同颜色线条
#可选择的colormap http://matplotlib.org/examples/color/colormaps_reference.html
#由于matplotlib不直接支持线状图的色谱，所以可能不易识别，所以使用尽可能不是那么连续的色谱，比如cubehelix
df = pd.DataFrame(np.random.randn(1000, 10), index=ts.index)
df = df.cumsum()
plt.show(df.plot(colormap="cubehelix",figsize=(10,10)))
plt.show(df.plot(colormap="rainbow",figsize=(10,10)))

#方法2：
from matplotlib import cm
plt.show(df.plot(colormap=cm.cubehelix))

#当然也能用于柱状图 
bars = pd.DataFrame(np.random.randn(10, 10)).applymap(abs)
bars = bars.cumsum()
plt.show(bars.plot.bar(colormap="cubehelix",figsize=(10,10)))
