# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 导入Axes3D类

fig = plt.figure()  # 获取到当前figure对象
fig.set_size_inches(10, 5)  # 设置图片尺寸，以inches为单位
ax = fig.gca(projection='3d')  # 获取图中的当前极轴（如果不存在或者不是极轴，则将创建相应的轴），返回的类型是Axes3D的子类

x = np.linspace(-10, 10, 1000)  # # 创建指定范围和元素数量的数组，这里x和y轴的范围都是[-10, 10]
y = np.linspace(-10, 10, 1000)  # 每一个点都由[x,y,z]三个坐标值来确定，x，y，z三个数组的元素数量应该相同
z = np.add(x, y)  # np.add是元素级（element-wise）的运算：将x和y两个数组的元素逐个相加，结果仍然是包含1000个元素的数组

ax.plot(x, y, z)  # 绘制3D线形图
plt.show()

# ### 立体绘图（3D plotting）
# 通过Matplotlib可以绘制3D图形；
# - Tutorials：https://matplotlib.org/tutorials/toolkits/mplot3d.html
# - Examples：https://matplotlib.org/gallery/index.html#d-plotting
# - API：https://matplotlib.org/api/toolkits/mplot3d.html
#
# ### Axes3D
# API：https://matplotlib.org/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html
# 本文涉及的绘制3D图形函数都位于此接口；
# 一些常用函数：
# - plot()：绘制3D线形图
# - scatter(): 绘制3D散点图
# - plot_wireframe()：绘制3D线框图
# - plot_surface()：绘制3D曲面图
# - contour()：绘制3D等高线
# - bar()：绘制3D柱状图
# - add_collection3d()：向图形中添加3D集合对象，可用来绘制3D多边形
