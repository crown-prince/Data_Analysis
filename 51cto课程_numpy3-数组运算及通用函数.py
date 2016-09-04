#numpy里面的一些内置的方法，函数以及numpy的基本运算
#numpy内置函数[即numpy中的通用函数(ufunc)]参考：http://docs.scipy.org/doc/numpy/reference/ufuncs.html

import numpy as np


def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")
    
#首先是numpy的基本运算，如加减乘除
arr1 = np.arange(10) #[0 1 2 3 4 5 6 7 8 9]
print(arr1)
arr2 = np.arange(1,20,2) #[ 1  3  5  7  9 11 13 15 17 19]
print(arr2)
make_end_line()
print(arr1 + arr2) #[ 1  4  7 10 13 16 19 22 25 28]
print(arr1 * arr2) #[  0   3  10  21  36  55  78 105 136 171]
print(arr1 / arr2) #[ 0.          0.33333333  0.4         0.42857143  0.44444444  0.45454545
                   #0.46153846  0.46666667  0.47058824  0.47368421]
print(arr1 - arr2) #[ -1  -2  -3  -4  -5  -6  -7  -8  -9 -10]
make_end_line()

#求numpy数组最大最小值
arr = np.arange(10)
print(arr)
print(arr.max()) #得数组中最大值
print(arr.min()) #得数组中最小值
make_end_line()

#all,any
lis1 = [1,0,3,5,False]
lis2 = [1,2,3,4]

arr1 = np.array(lis1)
arr2 = np.array(lis2)
print(arr1)
print(arr2)
print(arr1.all()) #所有为真为真，这里将输出False
print(arr2.any())  #任一为真则为真，这里将输出Ture
make_end_line()

#sqrt: 开平方 exp:计算各元素指数e的x次方
arr1 = np.arange(10)
print(arr1)
print(np.sqrt(arr1))
print(np.exp(arr1))
make_end_line()

#unique,sort
lis1 = [11,22,3,4,5,2,3,4,4,3]
arr = np.array(lis1)
print(arr)
print(np.unique(arr)) #取出数组中的元素,使其没有重复
arr.sort() #排序数组
print(arr)


#shape属性：通过shape属性来查看当前数组各个维度的大小
arr = np.arange(16).reshape((8, 2))
print(arr)
print(arr.shape) #(8, 2)


