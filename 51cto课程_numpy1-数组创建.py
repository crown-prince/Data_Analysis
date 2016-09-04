import numpy as np


def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")
    
#这里创建一个3x3的二维数组
n1 = np.arange(9).reshape((3,3)) #reshape()方法来更改数组的形状 是数组变为3x3的三维数组
print(n1)
print(n1[1][1]) #numpy数组的索引和python列表等相同，都从0开始
make_end_line()

#array方法创建数组,通过array方法，可接受一切序列型的对象，
#然后产生一个新的含有传入数据的numpy数组

data = [6, 7, 4, 8]
print(data, data[1])
arr = np.array(data)
print(arr, arr[1])
#嵌套的序列将会被转换为一个多维数组
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data)
print(arr)
make_end_line()


#通过arange，我们可以创建指定起始位置，终点位置，步长的一维数组
arr1 = np.arange(10) #[0 1 2 3 4 5 6 7 8 9]
arr2 = np.arange(1,11) #[ 1  2  3  4  5  6  7  8  9 10]
arr3 = np.arange(1, 11, 2) #[1 3 5 7 9]
print(arr1)
print(arr2)
print(arr3)
make_end_line()

lis1 = []
lis1 = range(10)
lis2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(lis1)
print(lis2, lis2[0][1])
arrtest = np.arange(10)
print(arrtest)
make_end_line()

#创建数组（随机）的一些方式，np.random：np.random.rand,np.random.randn
arr4 = np.random.randint(10)        #最大值为10
arr5 = np.random.randint(1, 10)     #最小值为1，最大值为10 np.random.randint(low[, high, size]) 返回随机的整数，位于半开区间 [low, high)
arr6 = np.random.randint(1, 10, 10) #最小值为1，最大值为10，数量为10
print(arr4)
print(arr5)
print(arr6)
print(np.random)
print(np.random.rand(5)) #np.random.rand 用于生成[0.0, 1.0)之间的随机浮点数，
                         #当没有参数时，返回一个随机浮点数，当有一个参数时，返回该参数长度大小的一维随机浮点数数组

print(np.random.randn(5)) #该函数返回一个样本，具有标准正态分布
make_end_line()



