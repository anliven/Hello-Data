# coding=utf-8
import pandas as pd

df = pd.DataFrame({
    'Name': ['A', 'A', 'A', 'B', 'B', 'C'],
    'Data': [666, 555, 444, 333, 222, 111]})
print('df=\n{}\n'.format(df))

# groupby
group_by = df.groupby('Name')  # 以“Name”列进行分组
for name, group in group_by:  # 分组后得到pandas.core.groupby.DataFrameGroupBy类型数据
    print("Name: {} - Group:\n{}\n".format(name, group))

# agg
print("Count by group: \n{}".format(group_by.count()))  # 直接调用，分组计数
print("Sum by group: \n{}".format(group_by.sum()))  # 分组求和
print("Mean by group: \n{}".format(group_by.mean()))  # 分组的平均值
print(group_by.agg([('Mean', 'mean'), ('Min', 'min'), ('Max', 'max')]))  # 通过agg一次性执行多个分组操作


def test_sort(data):
    """self-defining sort function"""
    return data.sort_values(by='Data', ascending=False)


# apply
print("Sort Group: \n{}".format(group_by.apply(test_sort)))

# ### 数据的分组与组合
# http://pandas.pydata.org/pandas-docs/stable/groupby.html
# 对批量的数据进行分组统计或者再处理
#
# ### 分组并处理数据
# - groupby：分组数据，便于进一步的统计或者处理
# - agg：对分组数据一次性执行多个操作（例如：median，std，var，prod，first，last等），可指定结果的列名
# - apply：通过将其他函数func应用到分组数据来处理分组数据
