import pandas as pd

def make_end_line(): #绘制下划线，用以分栏显示numpy各部分的作用
    for i in range(1, 50):
        print("_", end = "")
    print("\n")
    
ser = pd.Series(list("ABCDEFG"))
print(ser)
make_end_line()

#以下为ser显示(ser相当于一维数组)
"""
0    A
1    B
2    C
3    D
4    E
5    F
6    G
dtype: object

"""

import numpy as np
df = pd.DataFrame(np.random.randn(4, 6))
print(df)

#以下为df显示(df相当于二维数组)
"""
          0         1         2         3         4         5
0  0.012708  1.201418 -0.875854  1.206895  0.110769  1.216737
1 -0.581692  0.603498  1.270310 -0.228916  0.066367  0.748687
2 -0.912246 -1.848195 -0.080972  1.262782  2.715980  1.518973
3  0.305995 -0.766446 -0.841943  0.992780  0.834329 -2.910145

"""
