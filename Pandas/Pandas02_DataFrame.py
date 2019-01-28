# coding=utf-8
import pandas as pd
import numpy as np

# 创建DataFrame
df1 = pd.DataFrame(np.arange(9).reshape(3, 3))  # 通过NumPy创建一个3x3矩阵
df2 = pd.DataFrame(np.arange(9).reshape(3, 3),
                   columns=["Column1", "Column2", "Column3"],
                   index=["Row_a", "Row_b", "Row_c"])  # 创建时指定索引和列名
df3 = pd.DataFrame({"note": [1, 2, 3, "Fourth", "Fifth"],
                    "workday": ["Mon", "Tue", "Wed", "Thu", "Fri"]})  # 创建时指定列数据

# 访问数据
print("df1:\n{}\ndf2:\n{}\ndf3:\n{}\n".format(df1, df2, df3))
print("df3 workday:\n{}\n".format(df3['workday']))  # 类似数组方式，获取一列数据
print("df3 workday index 3:\n{}\n".format(df3['workday'][3]))  # 获取某个数据
# print("df3 workday:\n{}\n".format(df3.workday))  # 类似属性方式，获取一列数据，不建议此方式
# print("df3 workday index 3:\n{}\n".format(df3.workday[3]))  # 获取某个数据

# 更改数据
df3["Chr."] = pd.Series(["A", "B", "C", "D", "E"])  # 添加DataFrame列数据
print("df3:\n{}\n".format(df3))
del df3["note"]  # 删除DataFrame列数据
print("df3:\n{}\n".format(df3))

# 通过Series数组创建DataFrame
noteSeries = pd.Series(["1st", "2nd", "3rd", "4th"], index=[1, 2, 3, 4])
weekdaySeries = pd.Series(["100", "200", "300"], index=[1, 2, 3])
df4 = pd.DataFrame([noteSeries, weekdaySeries])  # 以Series数组来创建DataFrame，每个Series将成为一行，而不是一列
print("df4:\n{}\n".format(df4))

# ### Dataframe
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe
#   - DataFrame是2维表格结构，带有标签，大小可变，可以包含异构的数据列
#   - DataFrame可以简单理解为Series的容器，一个DataFrame中可以包含多个Series
#   - 默认的索引和列名都是[0, N-1]形式，可以在创建时指定索引和列名，索引可以任何类型的数据
#   - 以Series数组来创建DataFrame，每个Series将成为一行，而不是一列（如果Series索引不同，将以NaN值来填充内容）
