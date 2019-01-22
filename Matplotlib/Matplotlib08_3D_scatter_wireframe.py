# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

# 绘制3D散点图
ax = fig.add_subplot(1, 2, 1, projection='3d')  # 在同一个窗口中以矩阵的形式显示多个3D图形
count = 100
range_num = 100
xs = np.random.rand(count) * range_num
ys = np.random.rand(count) * range_num
zs = np.random.rand(count) * range_num
ax.scatter(xs, ys, zs, s=zs, c=zs)  # 参数c表示"A color", 参数s表示"Size in points^2"，这里根据z值的大小设置了点的颜色和尺寸
ax.set_xlabel('X Label')  # 设置坐标轴的Label
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 绘制3D线框图
ax = fig.add_subplot(1, 2, 2, projection='3d')  # 在同一个窗口中以矩阵的形式显示多个3D图形
x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(-np.power(X, 3), np.power(Y, 4))  # 构建数学函数为“z = -x^3 + y^4, -10<x,y<10”
ax.plot_wireframe(X, Y, Z)

plt.show()

# ### Axes3D
# API：https://matplotlib.org/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html
# 本文涉及的绘制3D图形函数都位于此接口；
# - scatter(): 绘制3D散点图
# - plot_wireframe()：绘制3D线框图
