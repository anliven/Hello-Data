# coding=utf-8
import pandas as pd

Series1 = pd.Series([' 1', '2 ', ' 3 ', '4', '5'])  # 包含空格字符串
print("Series1:\n{}\n".format(Series1))
print("Series1.str.rstrip():\n{}\n".format(Series1.str.lstrip()))
print("Series1.str.strip():\n{}\n".format(Series1.str.strip()))
print("Series1.str.isdigit():\n{}\n".format(Series1.str.isdigit()))  # str.isdigit()判断是否为数字

Series2 = pd.Series(['Test', 'Temp Test', 'This is a test !', 'AAA', 'bbb'])
print("Series2.str.lower():\n{}\n".format(Series2.str.lower()))  # 字符串小写
print("Series2.str.upper():\n{}\n".format(Series2.str.upper()))  # 字符串大写
print("Series2.str.len():\n{}\n".format(Series2.str.len()))  # 字符串长度

# ### 处理字符串
# http://pandas.pydata.org/pandas-docs/stable/api.html#string-handling
# Series.str字段包含一系列处理字符串的函数，而且这些函数会自动处理无效值
