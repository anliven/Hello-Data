# coding=utf-8
import numpy as np

base_data = np.arange(100, 200)  # 创建一个内容是 [100，200）区间的整数一维数组
print("base_data：\n{}\n".format(base_data))
base_data2 = base_data.reshape(10, -1)  # 转换为10X10的二维数组
print("base_data2 = np.reshape(base_data, (10, -1))：\n{}\n".format(base_data2))

# 通过下标来访问一维数组
print("base_data[10] = {}\n".format(base_data[10]))  # 通过指定下标array[index]的方式访问数组的元素

# 通过一维下标数组来访问一维数组
every_five = np.arange(0, 100, 5)
print("base_data[every_five]：\n{}\n".format(base_data[every_five]))  # 通过包含下标的数组来获取目标数组中的元素

# 通过多维下标数组来访问一维数组
matrix_two = np.array([(1, 2), (10, 20)])
print("matrix_two：\n{}\n".format(matrix_two))
print("base_data[matrix_two]：\n{}\n".format(base_data[matrix_two]))  # 实际上获取到一个2X2的矩阵

# 访问二维数组
print("base_data2[2]：{}\n".format(base_data2[2]))  # 只指定一个下标，访问到的是一个一维数组
print("base_data2[2, 3]：{}\n".format(base_data2[2, 3]))  # 指定两个下标，访问到的是具体的一个元素
print("base_data2[-1, -1]：{}\n".format(base_data2[-1, -1]))  # 通过”-1”来指定“最后一个”的元素

# 访问高维数组：形式类似二维数组

# 指定访问范围
print("base_data2[2, :]]：\n{}\n".format(base_data2[2, :]))  # 获取第2行的所有元素
print("base_data2[:, 3]]：\n{}\n".format(base_data2[:, 3]))  # 获取第3列的所有元素
print("base_data2[2:5, 2:4]]：\n{}\n".format(base_data2[2:5, 2:4]))  # 获取下标为[2,5)行，下标为[2,4)列的所有元素

# ### 索引
# Docs：https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
# 利用索引可以访问NumPy数组中的数据；
# 默认索引从0开始计数；
#
# # 指定访问范围
# 可以通过”:“的形式来指定范围，例如：2:5
# 只写”:“则表示全部范围
