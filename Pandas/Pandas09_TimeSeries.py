# coding=utf-8
import datetime as dt
import numpy as np
import pandas as pd

now = dt.datetime.now()  # 获得当前日期和时间
print("Now is {}".format(now))
yesterday = now - dt.timedelta(1)  # 通过timedelta函数执行日期加减
print("Yesterday is {}".format(yesterday.strftime('%Y-%m-%d')))

pd_day = pd.Timestamp('2019-01-05')  # 通过pd.Timestamp获得指定日期的时间戳
print("Weekday is {}".format(pd_day.day_name()))  # 获取对应的星期名称
print("Next day is {}".format(pd_day + pd.Timedelta('1 day')))  # 通过pd.Timedelta函数执行日期加减

this_year = pd.date_range(dt.datetime(2019, 1, 1),
                          dt.datetime(2019, 12, 31), freq='15D')  # 获取指定范围的日期序列，参数freq表示间隔时间，这里为15天
print("Selected days in 2019: \n{}\n".format(this_year))  # pandas.date_ranged的返回值是DatetimeIndex类型

df = pd.DataFrame(np.random.randint(0, 100, this_year.size),
                  index=this_year)  # 用DatetimeIndex作索引可以直接指定某个范围来选择数据
print("2019 Jan: \n{}\n".format(df['2019-01']))  # 

# ### 时间日期
# http://pandas.pydata.org/pandas-docs/stable/timeseries.html
# 除了datetime, time, calendar等几个标准模块外，Pandas提供多个函数用来生成和操作时间日期序列；
