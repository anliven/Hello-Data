# coding=utf-8
import numpy as np

zero_line = np.zeros((1, 3))  # 一行包含3个0的数组
one_column = np.ones((3, 1))  # 一列包含3个1的数组
print("zero_line = \n{}\n".format(zero_line))
print("one_column = \n{}\n".format(one_column))

a = np.array([(1, 2, 3), (4, 5, 6)])  # 一个2行3列的矩阵
b = np.arange(11, 20)  # 一个[11, 20)区间的整数一维数组
print("a = \n{}\n".format(a))
print("b = \n{}\n".format(b))

# 调整
b = b.reshape(3, -1)  # 通过reshape方法将其调整成为一个3行3列的矩阵，第二参数设为“-1”表示根据实际情况自动决定
print("b = b.reshape(3, -1)：\n{}\n".format(b))

# 拼接
c = np.vstack((a, b, zero_line))  # 通过vstack函数在垂直方向拼接三个数组
print("c = np.vstack((a,b, zero_line))：\n{}\n".format(c))
d = np.hstack((a.reshape(3, 2), b, one_column))  # 调整a数组后，通过hstack函数进行水平方向拼接
print("d = np.hstack((a,b, one_column))：\n{}\n".format(d))

# 拆分
e = np.hsplit(d, 3)  # 在水平方向指定数量平均拆分，这里将数组d拆分成3个数组
print("e = np.hsplit(d, 3)：\n{}\n".format(e))
print("e[1] = \n{}\n".format(e[1]))  # 打印下标是1的e[1]数组
f = np.hsplit(d, (1, 3))  # 在水平方向指定列数进行拆分，这里将数组d从第1列和第3列两个地方进行拆分
print("f = np.hsplit(d, (1, 3))：\n{}\n".format(f))
g = np.vsplit(d, 3)  # 在垂直方向进行平均拆分，这里将数组d拆分成3个数组
print("g = np.vsplit(d, 3)：\n{}\n".format(g))

# ### Shape与操作
# Docs：https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html
# 利用现有函数可以根据已有数组来产生一些新的数据结构
# - reshape：根据已有数组和指定的shape，生成一个新的数组
# - vstack：将多个数组在垂直（v代表vertical）方向拼接（数组的维度必须匹配）
# - hstack：将多个数组在水平（h代表horizontal）方向拼接（数组的维度必须匹配）
# - hsplit：将数组在水平方向拆分
# - vsplit：将数组在垂直方向拆分
# 特别注意：
# - 如果两个数组的结构是不兼容的，拼接将无法完成；
# - 如果设置的拆分数量使得原先的数组无法平均拆分，操作将会失败；
