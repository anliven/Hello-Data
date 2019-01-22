# coding=utf-8
import numpy as np

print(np.__version__)

# 基础属性与数组创建
data1 = [1, 2, 3]  # NumP认为这是一个具有rank 1的数组，axis的长度为3
data2 = [[1, 2, 3], [4, 5, 6]]  # NumP认为这是一个具有rank 2的数组，axis的长度也是3
print('Type: ', type(data1), type(data2))

a = np.array([1, 2, 3], dtype=complex)  # 通过array函数来创建指定元素类型和内容的NumPy数组
b = np.array([(1, 2, 3), (4, 5, 6)], np.int64)  # 注意必须为方括号
print('Type: ', type(a), type(b))
print('a= ', a)
print("a's ndim:{} shape:{} size:{} dtype:{} itemsize:{}".format(a.ndim, a.shape, a.size, a.dtype, a.itemsize))
print('b= ', b)
print("b's ndim:{} shape:{} size:{} dtype:{} itemsize:{}".format(b.ndim, b.shape, b.size, b.dtype, b.itemsize))

# 特定array的创建
sa = np.zeros((2, 3))  # 创建元素全部是0的数组
sb = np.ones((2, 3))  # 创建元素全部是1的数组
sc = np.empty((2, 3))  # 创建未初始化数据的数组，因此是内容是不确定的
sd = np.arange(1, 3, 0.3)  # 创建指定范围和步长的数组
se = np.linspace(2.0, 3.0, num=5)  # 创建指定范围和元素数量的数组
sf = np.random.random((2, 3))  # 创建随机数的数组
print('sa:{}\nsb:{}\nsc:{}\nsd:{}\nse:{}\nsf:{}'.format(sa, sb, sc, sd, se, sf))

# ### NumPy
# HomePage：http://www.numpy.org/
# NumPy（数值 Python 的简称）是用Python实现的用于科技计算的基础软件包，是一个强大的科学分析和建模工具
# - 提供了大量数据结构，能够轻松地执行多维数组和矩阵运算
# - 可用作不同类型通用数据的多维容器
# - 可以和其他编程语言无缝集成
# - 可以简单而快速地与大量数据库和工具结合
#
# ### 文档信息
# - HomePage：http://www.numpy.org/
# - Manual：https://docs.scipy.org/doc/numpy/
# - User Guide：https://docs.scipy.org/doc/numpy/user/
# - Reference：https://docs.scipy.org/doc/numpy/reference/generated/
# - Function Index：https://docs.scipy.org/doc/numpy/genindex.html
#
# ### 基础属性与数组创建
# NumPy的基础是一个同构的多维数据，数组中的元素可以通过下标来索引。
# 在NumPy中，维度称之为axis（复数是axes），维度的数量称之为rank。
#
# ### 数组类ndarray
# Docs：https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html
# NumPy的数组类是ndarray，别名numpy.array，具有以下的属性：
# - ndarray.ndim：数组的维数，称之为rank
# - ndarray.shape：数组的维度，由一系列数字组成。例如：长度为n的一维数组的shape是n。一个n行m列的矩阵的shape是n,m
# - ndarray.size：数组中所有元素的数量
# - ndarray.dtype：数组中元素的类型，例如：numpy.int32, numpy.int16或者numpy.float64
# - ndarray.itemsize：数组中每个元素的大小，单位为字节
# - ndarray.data：存储数组元素的缓冲，通常只需要通过下标来访问元素，而不需要访问缓冲
#
# ### 特定array的创建
# Docs：https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html
# 通过现有的辅助函数可以创建特定的数组
