# coding=utf-8
import numpy as np

# 随机数
print("random:\n{}\n".format(np.random.random(10)))  # 生成包含10个元素在[0.0, 1.0)之间的一维随机数组
print("random:\n{}\n".format(np.random.random((5, 4))))  # 生成5行4列，元素在[0.0, 1.0)之间的二维随机数组
print("rand:\n{}\n".format(np.random.rand(3, 4)))  # 根据指定的shape生成随机数
print("randint:\n{}\n".format(np.random.randint(0, 100, 20)))  # 生成指定范围内（[0, 100)）的指定数量（20）的随机整数
print("permutation:\n{}\n".format(np.random.permutation(np.arange(20))))  # 随机打乱已有的数据顺序

# 数学运算
base_data = (np.random.random((5, 5)) - 0.5) * 100
print("base_data = \n{}\n".format(base_data))
print("np.amin：{} np.amax：{} np.average：{} np.sum：{}".format(
    np.amin(base_data),
    np.amax(base_data),
    np.average(base_data),
    np.sum(base_data)))
print("np.sin(base_data) = \n{}".format(np.sin(base_data)))

# 常见运算
print(np.floor(np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])))  # np.floor返回不大于输入参数的最大整数，向下取整
print(np.ceil(np.array([-1.7, -2.5, -0.2, 0.6, 1.2, 2.7, 11])))  # np.ceil返回输入值的上限，向上取整
print(np.around(np.array([-0.746, 4.6, 9.4, 7.447, 10.455, 11.555]), decimals=2))  # np.around返回四舍五入后的值，可指定精度

# ### 随机数
# Docs：https://docs.scipy.org/doc/numpy/reference/routines.random.html
# 利用numpy.random包中的随机数算法可以生成多种随机数据；
#
# ### 数学运算
# Docs：https://docs.scipy.org/doc/numpy/reference/routines.math.html
