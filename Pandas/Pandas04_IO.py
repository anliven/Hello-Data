# coding=utf-8
import pandas as pd

df1 = pd.read_excel(path="./Ztest.xlsx")  # 读取Excel文件（需要安装xlrd库）
print("df1:\n{}\n".format(df1))

df2 = pd.read_csv(path="./Ztest.csv", sep="|")  # 读取csv文件（默认通过逗号分隔）
print("df2:\n{}\n".format(df2))

# ### IO Tools
# http://pandas.pydata.org/pandas-docs/stable/io.html#
# pandas库提供了一系列的read_函数来读取各种格式的文件
# 常见的函数：
#   - CSV       read_csv	  to_csv
#   - JSON      read_json	  to_json
#   - HTML      read_html	  to_html
#   - MS Excel  read_excel    to_excel
#   - SQL       read_sql	  to_sql
#
# ### CSV & Text files
# http://pandas.pydata.org/pandas-docs/stable/io.html#csv-text-files
# 一些参数：
#   - path           文件路径
#   - sep            字段分隔符
#   - header         列名的行数，默认是0（第一行）
#   - index_col      列号或名称用作结果中的行索引
#   - names          结果的列名称列表
#   - skiprows       从起始位置跳过的行数
#   - na_values      代替NA的值序列
#   - comment        以行结尾分隔注释的字符
#   - parse_dates    尝试将数据解析为datetime。默认为False
#   - converters     列的转换器
#   - data_parser    用来解析日期的函数
#   - nrows          从文件开始读取的行数
#   - skip_footer    文件末尾需要忽略的行数
#   - verbose        输出各种解析输出的信息
#   - encoding       文件编码
#   - squeeze        如果解析的数据只包含一列，则返回一个Series
#   - thousands      千数量的分隔符
