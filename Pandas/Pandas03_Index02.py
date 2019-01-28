# coding=utf-8
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('max_colwidth', 100)  # 设置value的显示长度为100，默认为50

index_a = pd.Index(['A', 'B', 'C', 'aaa', 555], name='ChrA')  # 通过数组创建Index对象，参数name指定索引名
index_b = pd.Index(['aaa', 'bbb', 'ccc', 'A', 555], name='ChrB')
print("a：{}\nb：{}\n".format(index_a, index_b))
print("a|b = {}".format(index_a | index_b))
print("a&b = {}".format(index_a & index_b))
print("a.difference(b) = {}".format(index_a.difference(index_b)))
print("b.difference(a) = {}".format(index_b.difference(index_a)))

# MultiIndex
multiIndex = pd.MultiIndex.from_arrays([
    ['AAA', 'AAA', 'AAA', 'AAA', 'BBB', 'BBB', 'BBB', 'BBB', 'CCC', 'CCC', 'CCC', 'CCC', ],
    ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4']],
    names=('Company', 'Turnover'))
print("multiIndex = \n{}\n".format(multiIndex))
df = pd.DataFrame(data=np.random.randint(100, 500, 36).reshape(-1, 12),
                  index=[2016, 2017, 2018],
                  columns=multiIndex)
print("df = \n{}\n".format(df))

print("df 2017 Q1 = \n{}\n".format(df.loc[2017, (['AAA', 'BBB', 'CCC'], 'Q1')]))  # 通过多级索引筛选数据
print("df Company AAA = \n{}\n".format(df.loc[2018, 'AAA']))

# ### Index对象
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.html
# pandas.Index类提供多种对Index对象的操作方法
# 常见子类：
#   - RangeIndex
#   - CategoricalIndex
#   - MultiIndex
#   - IntervalIndex
#   - DatetimeIndex, TimedeltaIndex, PeriodIndex, Int64Index, UInt64Index, Float64Index
#
# ### MultiIndex
# A multi-level, or hierarchical, Index
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.MultiIndex.html
# 数据的行或者列通过多层次的标签来进行索引
# 通过多级索引，可以方便进行数据筛选
