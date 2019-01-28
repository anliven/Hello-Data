# coding=utf-8
import pandas as pd

# Series
s = pd.Series(["1st", "2nd", "3rd", 444], index=["A", "A", "B", 4])  # 索引并非集合，可以包含重复的数据
print("Series:\n{}\n".format(s))
print("Series index A:\n{}\n".format(s.loc["A"]))  # 访问相同索引下的所有内容
print("Series:\n{}\n".format(s.iloc[[0, 1, 3]]))  # 通过index的下标访问数据（注意不是值，而且只有一个下标）

# DataFrame
df = pd.DataFrame({"note": ["1st", "2nd", "3rd", "4th", "5th"],
                   "workday": ["Mon", "Tue", "Wed", "Thu", "Fri"]},
                  index=["AAA", "AAA", "BBB", "CCC", 555])  # 创建时指定列数据
print("df:\n{}\n".format(df))
print("df.columns:\n{}\n".format(df.columns))  # 获取DataFrame列的Index对象
print("df.index:\n{}\n".format(df.index))  # 获取DataFrame行的Index对象
# loc
print("Note AAA is:\n{}\n".format(df.loc["AAA"]))  # 访问整行数据（只指定一个索引）
print("Note AAA BBB is:\n{}\n".format(df.loc[["AAA", "BBB"], "note"]))  # 访问行索引为"AAA"和"BBB"，列索引为“note”的元素
# iloc
print("Note AAA is:\n{}\n".format(df.iloc[[0, 1]]))  # 访问整行数据（只指定行下标）
print("Note AAA 555 is:\n{}\n".format(df.iloc[[0, 1, 4], 0]))  # 访问行下标为0、1和4，列下标为0的元素

# 访问某个范围的数据（分片，Slicing with labels）
print("Series.loc['A':3]=\n{}\n".format(s.loc['A':'B']))
# print("Series.loc['A':3]=\n{}\n".format(s.loc['A':4]))  # 注意此行报错
print("df.iloc[2:4]=\n{}\n".format(df.iloc[2:4]))

# 访问单个元素值
print("Series.at['A']={}\n".format(s.at['A']))  # 访问索引‘A’的数据
print("df.iat[3,1]={}\n".format(df.iat[3, 1]))  # 访问3行1列的数据

# ### Indexing and Selecting Data
# http://pandas.pydata.org/pandas-docs/stable/indexing.html
#   - Index对象的值不可以改变，因此可以通过它安全的访问数据
#   - Index的值可以是整数
#   - Index并非集合，可以包含重复的数据
#
# ### 访问数据
#   - loc：通过行和列的索引来访问数据，可访问整行数据和单个数据
#   - iloc：通过行和列的下标来访问数据，可访问整行数据和单个数据
#
# ### 访问单个元素值（Scalar Value）
#   - at：通过行和列的索引来访问数据
#   - iat：通过行和列的下标来访问数据
