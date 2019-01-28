# coding=utf-8
import pandas as pd

series1 = pd.Series([1, 2, 3])  # Series是一维结构的数据，可以直接通过数组来创建
print("Series1:\n{}".format(series1))  # 打印内容，注意最后一行显示的数据类型
print("series1.values: {}".format(series1.values))  # 打印Series的数据
print("series1.index: {}".format(series1.index))  # 打印Series的索引

series2 = pd.Series([4, 5, 6], index=["D", "Five", 666])  # 创建时指定索引
print("Series2:\n{}".format(series2))
print("Five is {}".format(series2["Five"]))  # 类似数组的访问数据方式
# print("Five is {}".format(series2.Five))  # 类似属性的访问方式，不建议此方式
# print("666 is {}".format(series2.666))  # 类似属性的访问方式要求索引元素必须是有效的Python标识符，否则将报错

series3 = pd.Series(["1st", "2nd", "3rd"], index=[1, 2, 2])  # 索引并非集合，可以包含重复的数据
print("Series3:\n{}".format(series3))
print("series3 index 2:\n{}".format(series3["2"]))  # 访问相同索引下的所有内容

# ### Data Structures
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html
# 两个核心数据结构是Series和DataFrame
#
# ### Series
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#series
#   - Series是1维数组结构，带有标签的同构类型数组
#   - 默认索引是[1, N-1]形式，也可以在创建时指定索引，索引可以任何类型的数据
#   - 索引并非集合，可以包含重复的数据
