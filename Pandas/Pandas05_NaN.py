# coding=utf-8
import pandas as pd
import numpy as np

Series1 = pd.Series(["1st", "2nd", "3rd", np.nan])  # np.nan为无效值
Series2 = pd.Series(["aaa", "bbb", np.nan])
Series3 = pd.Series([111, 222])
Series4 = pd.Series(["AAA"])

df = pd.DataFrame([Series1, Series2, Series3, Series4])  # 创建含有无效值的DataFrame
print("df:\n{}\n".format(df))

print("df NaN:\n{}\n".format(pd.isna(df)))  # 通过pandas.isna函数确认无效值

# 忽略无效值
print("df.dropna():\n{}\n".format(df.dropna()))  # 通过pandas.DataFrame.dropna函数忽略无效值，默认参数“axis=0，how='any'”
# print("df.dropna():\n{}\n".format(df.dropna(inplace=True)))  # 直接更改数据本身
# print("df:\n{}\n".format(df))
print("df.dropna(axis=1, how='all'):\n{}\n".format(df.dropna(axis=1, how='all')))  # 忽略整列都是无效值的列
print("df.dropna(axis=0, how='all'):\n{}\n".format(df.dropna(axis=0, how='all')))  # 忽略整行都是无效值的行

# 替换无效值
print("df.fillna('Temp'):\n{}\n".format(df.fillna('Temp')))  # 通过pandas.DataFrame.fillna函数将无效值统一替换成为有效值
df.rename(index={0: 'index1', 1: 'index2', 2: 'index3', 3: 'index4'},
          columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4'},
          inplace=True)  # 为了便于操作，在填充前先通过rename方法修改行和列的名称
df.fillna(value={'col2': 200}, inplace=True)  # 指定不同的数据进行填充
df.fillna(value={'col3': 999}, inplace=True)
df.fillna(value={'col4': "Test"}, inplace=True)
print("df:\n{}\n".format(df))

# ### Working with missing data
# http://pandas.pydata.org/pandas-docs/stable/missing_data.html
# 处理无效值的主要方法：直接忽略无效值，或者将无效值替换成有效值
#
# ### 确认无效值
# 通过pandas.isna函数确认无效值，以“False”或“True”来标记是否为无效
#
# ### 忽略无效值
# 通过pandas.DataFrame.dropna函数忽略无效值
# dropna默认不会改变原先的数据结构，而是返回了一个新的数据结构
# 在调用函数时传递参数“inplace=True”，可直接更改数据本身
# 设置参数axis和how可以忽略都是无效值的整列或整列，默认值“axis=0，how='any'”表示忽略包含任意无效值的行
#
# ### 替换无效值
# 通过fillna函数将无效值替换成为有效值
# 可以键将无效值统一替换成为有效值，也可以指定不同的数据进行填充
