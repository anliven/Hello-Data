# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(-np.power(X, 3), np.power(Y, 2))  # 构建数学函数：“z = -x^3 + y^2, -10<x, y<10”

fig = plt.figure()

# 绘制3D曲面图
ax = fig.add_subplot(2, 1, 1, projection='3d')  # 在同一个窗口中以矩阵的形式显示多个3D图形
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)  # 参数cmap指定曲面颜色
fig.colorbar(surf, shrink=0.5, aspect=5)  # 添加色彩条，参数shrink指定色彩条与图形高度的比例，参数aspect指定色彩条本身的长宽比

# 绘制3D等高线
ax = fig.add_subplot(2, 1, 2, projection='3d')  # 在同一个窗口中以矩阵的形式显示多个3D图形
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.plot_wireframe(X, Y, Z, alpha=0.1)  # 参数alpha设置透明度，便于观察
ax.contour(X, Y, Z, cmap=cm.Accent, linewidths=2)  # 参数linewidths设置等高线粗度

plt.show()

# ### Colormap
# Matplotlib内置多种Colormap可以简化图形着色的过程，通过指定相应的名称就可以直接使用相应的Colormap
# https://matplotlib.org/users/colormaps.html
#
# ### Axes3D
# API：https://matplotlib.org/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html
# 本文涉及的绘制3D图形函数都位于此接口；
# - plot_surface()：绘制3D曲面图
# - contour()：绘制3D等高线
