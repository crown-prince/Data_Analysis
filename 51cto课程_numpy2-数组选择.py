import numpy as np


def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")

def main():
    #一维数组
    print("一维数组: ")
    arr1 = np.arange(10)
    print(arr1)
    make_end_line()
    print(arr1[1]) #取第一个数字
    print(arr1[1:5]) #取1到5
    print(arr1[1:5:2]) #取1到5中间隔为2
    print(arr1[:5]) #只指定终点
    print(arr1[::2]) #只指定步长

    #二维数组
    print("\n二维数组: ")
    arr2 = np.arange(15).reshape((3,5)) #生成一个三行5列的数组 
    print(arr2)
    make_end_line()
    print(arr2[1], "\n") #取索引为1的行
    print(arr2[1:3], "\n") #取索引为1到3的行
    print(arr2[1:3:2], "\n") #取索引为1的行，步长为2
    print(arr2[:3],"\n") #只指定终点
    print(arr2[::2],"\n")  #只指定数组间步长 
    make_end_line()
    print(arr2[1][2], "\n") #取索引为[1][2]的数
    print(arr2[1][1:5], "\n") #取索引在[1] 而列在1到5之间的数
    print(arr2[1:3,2:4], "\n") #取第1，第2行，第3，第4个数
if __name__ == "__main__":
    main()
    
