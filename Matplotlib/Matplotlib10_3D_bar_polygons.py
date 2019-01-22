# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

# 绘制3D柱状图
ax = fig.add_subplot(1, 2, 1, projection='3d')
np.random.seed(59)
month = np.arange(1, 12)
years = [2016, 2017, 2018, 2019]


def get_color(value_array):
    color = []
    for v in value_array:
        if v < 50:
            color.append('y')
        elif v < 100:
            color.append('g')
        elif v < 150:
            color.append('b')
        elif v < 200:
            color.append('c')
        elif v < 250:
            color.append('m')
        else:
            color.append('r')
    return color


for year, c in zip(years, ['b', 'c', 'r', 'm']):
    value = np.random.rand(len(month)) * 300
    ax.bar(month, value, year, zdir='y', color=get_color(value), alpha=0.7)
    for i in np.arange(0, 12):
        ax.bar

ax.set_xlabel('Month')
ax.set_xticks(np.arange(1, 13))
ax.set_ylabel('Year')
ax.set_yticks(np.arange(2016, 2020))
ax.set_zlabel('Precipitation')

# 绘制3D多边形
ax = fig.add_subplot(1, 2, 2, projection='3d')
precipitation = []
for year in years:
    value = np.random.rand(len(month)) * 300
    value[0], value[-1] = 0, 0
    precipitation.append(list(zip(month, value)))

poly = PolyCollection(precipitation, facecolors=['b', 'c', 'r', 'm'])
poly.set_alpha(0.7)

ax.add_collection3d(poly, zs=years, zdir='y')
ax.set_xlabel('Month')
ax.set_xlim3d(0, 12)
ax.set_ylabel('Year')
ax.set_ylim3d(2015, 2020)
ax.set_zlabel('Precipitation')
ax.set_zlim3d(0, 300)

plt.show()

# ### Axes3D
# API：https://matplotlib.org/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html
# 本文涉及的绘制3D图形函数都位于此接口；
#   - bar()：绘制3D柱状图
#   - add_collection3d()：向图形中添加3D集合对象，可用来绘制3D多边形
# 本文图形内容是对比一个城市四年期间每个月的降水量;
#
# 官网示例
#   - 3D柱状图：https://matplotlib.org/gallery/mplot3d/bars3d.html#sphx-glr-gallery-mplot3d-bars3d-py
#   - 3D多边形：https://matplotlib.org/gallery/mplot3d/polys3d.html#sphx-glr-gallery-mplot3d-polys3d-py
