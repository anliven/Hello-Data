# coding=utf-8
import pandas as pd

df = pd.DataFrame({"note": ["1st", "2nd", "3rd", "4th", "5th"],
                   "workday": ["Mon", "Tue", "Wed", "Thu", "Fri"]},
                  index=["AAA", "AAA", "BBB", "CCC", "DDD"])  # 创建时指定列数据

print("df：\n{}".format(df))
print("df.columns：{}".format(df.columns))  # 获取DataFrame的列对象
print("df.index：{}".format(df.index))  # 获取DataFrame中行的Index对象
print("Note AAA BBB is:\n{}\n".format(df.loc[["AAA", "BBB"], "note"]))  # 访问行索引为"AAA"和"BBB"，列索引为“note”的元素
print("Note AAA CCC is:\n{}\n".format(df.iloc[[0, 1, 3], 0]))  # 访问行下标为0、1和3，列下标为0的元素

# ### Indexing and Selecting Data
# http://pandas.pydata.org/pandas-docs/stable/indexing.html
# Index对象的值不可以改变，因此可以通过它安全的访问数据
# Index并非集合，可以包含重复的数据
#
# ### 访问DataFrame中的数据
#  - loc：通过行和列的索引来访问数据
#  - iloc：通过行和列的下标来访问数据
