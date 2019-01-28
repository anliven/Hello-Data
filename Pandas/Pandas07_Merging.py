# coding=utf-8
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Note': [111, 222], 'Weekday': ['Mon', 'Tue']}, index=[1, 2])
df2 = pd.DataFrame({'Note': [333, 444], 'Weekday': ['Wed', 'Thu']}, index=[3, 4])
df3 = pd.DataFrame({'Note': [555, 666], 'Weekday': ['Fri', 'Sat']}, index=[5, 6])
df4 = pd.DataFrame({'Note': [777], 'Weekday': ['Sun']}, index=[7])

# concat
df_concat = pd.concat([df1, df2, df3, df4], keys=['df1', 'df2', 'df3', 'df4'])
print("df_concat=\n{}\n".format(df_concat))  # concat函数默认将多个数据纵向串联，结果存在MultiIndex
df_concat_column = pd.concat([df1, df2, df3, df4], axis=1)  # 指定参数“axis=1”以列为主进行串联
print("df_concat_column=\n{}\n".format(df_concat_column))  # 其余数据以“NaN”填充

# append
df_append = df1.append([df2, df3, df4])  # append函数在原数据基础上添加其他数据来进行串联，结果与原数据结构相同
print("df_append=\n{}\n".format(df_append))

# merge
df5 = pd.DataFrame({'Key': ['key1', 'key2', 'key3'], 'A': ['a1', 'a2', 'a3'], 'B': ['b1', 'b2', 'b3']})
df6 = pd.DataFrame({'Key': ['key3', 'key6', 'key9'], 'A': ['a3', 'a6', 'a9'], 'B': ['b3', 'b6', 'b9']})
print("df5=\n{}\ndf6=\n{}\n".format(df5, df6))
merge_df = pd.merge(df5, df6)  # merge函数默认inner方式（内连接，也就是获得键的交集）
merge_inner_key = pd.merge(df5, df6, how='inner', on=['Key'])  # 参数on表示将当作连接键的列名
print("merge_df=\n{}\nmerge_inner=\n{}\n".format(merge_df, merge_inner_key))
merge_left = pd.merge(df5, df6, how='left')  # 左连接
merge_left_key = pd.merge(df5, df6, how='left', on=['Key'])
print("merge_left=\n{}\nmerge_left_key=\n{}\n".format(merge_left, merge_left_key))
merge_right = pd.merge(df5, df6, how='right')  # 右连接
merge_right_key = pd.merge(df5, df6, how='right', on=['Key'])
print("merge_right=\n{}\nmerge_right_key=\n{}\n".format(merge_right, merge_right_key))
merge_outer = pd.merge(df5, df6, how='outer')  # 外连接，也就是获得键的并集
merge_outer_key = pd.merge(df5, df6, how='outer', on=['Key'])
print("merge_outer=\n{}\nmerge_outer_key=\n{}\n".format(merge_outer, merge_outer_key))

# join
df7 = pd.DataFrame({'Key': ['key1', 'key2', 'key3'],
                    'A': ['a1', 'a2', 'a3'],
                    'B': ['b1', 'b2', 'b3']},
                   index=[0, 1, 2])  # 注意索引
df8 = pd.DataFrame({'Key': ['key3', 'key6', 'key9'],
                    'A': ['a3', 'a6', 'a9'],
                    'B': ['b3', 'b6', 'b9']},
                   index=[1, 2, 3])  # join函数可被用于合并多个DataFrame（具有相同的或者类似索引）
print("df7=\n{}\ndf8=\n{}\n".format(df7, df8))
join_left = df7.join(df8, how='left', lsuffix='_self', rsuffix='_other')  # join函数根据索引进行数据合并，默认是左连接
join_right = df7.join(df8, how='right', lsuffix='_self', rsuffix='_other')  # 通过参数lsuffix和rsuffix可以区分结果的列名
print("join_left=\n{}\njoin_right=\n{}\n".format(join_left, join_right))
join_inner = df7.join(df8, how='inner', lsuffix='_self', rsuffix='_other')
join_outer = df7.join(df8, how='outer', lsuffix='_self', rsuffix='_other')
print("join_inner=\n{}\njoin_outer=\n{}\n".format(join_inner, join_outer))

# ### 数据整合
# http://pandas.pydata.org/pandas-docs/stable/merging.html
#
# ### 理解merge和join中的连接方式
# - inner：只返回两张表中都满足on条件的记录
# - outer：返回两张表中的所有记录，对于不满足on条件一端的记录用NaN替换
# - left：返回“表名1”的全部行，对于“表名2”中，不满足on条件的记录用NaN替换
# - right：返回“表名2”的全部行，对于“表名1”中，不满足on条件的记录用NaN替换
