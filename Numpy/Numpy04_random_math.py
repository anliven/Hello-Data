# coding=utf-8
import numpy as np

# 随机数
print("random:\n{}\n".format(np.random.random(10)))  # 生成包含10个元素在[0.0, 1.0)之间的一维随机数组
print("random:\n{}\n".format(np.random.random((5, 4))))  # 生成5行4列，元素在[0.0, 1.0)之间的二维随机数组
print("rand:\n{}\n".format(np.random.rand(3, 4)))  # 根据指定的shape生成随机数
print("randint:\n{}\n".format(np.random.randint(0, 100, 20)))  # 生成指定范围内（[0, 100)）的指定数量（20）的随机整数
print("permutation:\n{}\n".format(np.random.permutation(np.arange(20))))  # 随机打乱已有的数据顺序

# 数学运算
base_data = np.random.randint(0, 100, 25).reshape(5, -1)  # 随机生成一个元素值在（[0, 100)）内的5行5列整数矩阵
print("base_data = \n{}\n".format(base_data))
print("np.amin：{} np.amax：{} np.average：{} np.sum：{} \n".format(
    np.amin(base_data),
    np.amax(base_data),
    np.average(base_data),
    np.sum(base_data)))

base_data2 = np.array([(-0.746, -0.2, -1.5, 2.0), (9.4, 7.447, 10, 11.555)])
print("base_data2 = \n{}\n".format(base_data2))
print("np.floor(base_data2)):\n", np.floor(base_data2))  # 返回不大于输入参数的最大整数，向下取整
print("np.ceil(base_data2)):\n", np.ceil(base_data2))  # 返回输入值的上限，向上取整
print("np.around(base_data2)):\n", np.around(base_data2, decimals=2))  # 返回四舍五入后的值，可指定精度
print("np.where(base_data2)):\n", np.where(base_data2 >= 3))  # 返回所有值大于等于3的元素的索引
print("np.diff(base_data2)):\n", np.diff(base_data2))  # 返回相邻元素的差（后一个元素值减去前一个元素值）
print("np.msort(base_data2)):\n", np.msort(base_data2))  # 数组排序

base_data3 = np.array([(3, 21, 10), (2, 9, 23), (11, 5, 17)])
print("\nbase_data3 = \n{}\n".format(base_data3))
print("tolist：{}\n".format(base_data3.tolist()))  # 返回python的list
print("clip：{}\n".format(base_data3.clip(2, 5)))  # 小于2的元素替换为2，大于5的元素替换为5
print("max：{} min：{} ptp：{} \n".format(base_data3.max(),
                                       base_data3.min(),
                                       base_data3.ptp()))  # 返回所有元素的最大值、最小值、最大值和最小值之差
print("var：{} std：{}\n".format(base_data3.var(),
                               base_data3.std()))  # 返回方差（元素与均值之差的平方的均值）、标准差（方差的算术平方根）
print("sum：{} prod：{} mean：{} \n".format(base_data3.sum(),
                                         base_data3.prod(),
                                         base_data3.mean()))  # 返回所有元素的和、乘积、算术平均值
print("argmin：{} argmax：{}\n".format(base_data3.argmin(),
                                     base_data3.argmax()))  # 返回最小值、最大值在扁平数组中的索引

base_data4 = np.array([3, 2, 4, 1, 5])
print("\nbase_data4 = \n{}\n".format(base_data4))
print("np.log(base_data4)): ", np.log(base_data4))  # 返回对数数组
print("np.exp(base_data4)): ", np.exp(base_data4))  # 返回指数数组
print("np.sqrt(base_data4)): ", np.sqrt(base_data4))  # 返回开方数组
print("np.power(base_data4, 3)): ", np.power(base_data4, 3))  # 返回3次方数组

# ### 随机数
# Docs：https://docs.scipy.org/doc/numpy/reference/routines.random.html
# 利用numpy.random包中的随机数算法可以生成多种随机数据；
#
# ### 数学运算
# Docs：https://docs.scipy.org/doc/numpy/reference/routines.math.html
