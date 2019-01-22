# coding=utf-8
import numpy as np

base_data = np.floor((np.random.random((3, 3)) - 0.5) * 10)
print("base_data = \n{}\n".format(base_data))

# 矩阵的转置
print("base_data.T = \n{}\n".format(base_data.T))  # 通过.T获得矩阵的转置
print("base_data.transpose() = \n{}\n".format(base_data.transpose()))  # 通过transpose函数获得矩阵的转置

# 矩阵的乘法
matrix_one = np.ones((3, 3))
print("matrix_one = \n{}\n".format(matrix_one))
minus_one = np.dot(matrix_one, -1)  # 通过dot函数进行矩阵的乘法
print("minus_one = \n{}\n".format(minus_one))
print("np.dot(base_data, minus_one) = \n{}\n".format(np.dot(base_data, minus_one)))

# 从坐标向量返回坐标矩阵
x = np.arange(1, 4)  # 生成一维数组，也就是向量
y = np.arange(201, 205)
print(x, y)
a, b = np.meshgrid(x, y)  # #将两个一维数组变为二维矩阵：将x变成了矩阵a的行向量，y变成了矩阵b的列向量
print("a:\n{}\nb:\n{}".format(a, b))

# ### 矩阵
# Docs：https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
#
# # 矩阵的转置
# numpy.ndarray.T：https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.T.html
# numpy.matrix.transpose：https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.transpose.html
#
# # 矩阵的乘法
# numpy.dot：https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html
#
# # 从坐标向量返回坐标矩阵
# numpy.meshgrid：https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html
# meshgrid函数可以从一个坐标向量中返回一个坐标矩阵，可简单理解为互相由对方数据的数量来确定尺寸;
