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

# ### 矩阵
# Docs：https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
#
# # 矩阵的转置
# numpy.ndarray.T：https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.T.html
# numpy.matrix.transpose：https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.transpose.html
#
# # 矩阵的乘法
# numpy.dot：https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html
