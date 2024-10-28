# -*- coding:utf-8 -*-
import pandas as pd

df1 = pd.DataFrame([[1, 2], [3, 4], [9, 9]])
df2 = pd.DataFrame([[5, 6], [7, 8]])

df = pd.concat([df1, df2], ignore_index=True)

print("df1的值为:")
print(df1)
print("df2的值为:")
print(df2)
print("df的值为:")
print(df)
"""
运行结果：
df1的值为:
   0  1
0  1  2
1  3  4
df2的值为:
   0  1
0  5  6
1  7  8
df的值为:
   0  1
0  1  2
1  3  4
2  5  6
3  7  8
"""
