# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.figure(figsize=(10, 5))  # 参数figsize设置尺寸(width, height)以inches为单位

plt.pie(np.random.rand(7) * 100, labels=labels, autopct='%1.1f%%')  # autopct指定数值的精度格式
plt.axis('equal')  # 坐标轴大小一致
plt.legend()  # 绘制图例

filename = "./" + "TestSaveFile.png"
plt.savefig(filename, dpi=200, format='png')  # 保存文件，必须在plt.show()之前使用，否则保存的文件将是空白内容

plt.show()  # plt.show()后实际上已经创建了一个新的空白图片

# ### 饼状图（matplotlib.pyplot.pie）
# 饼状图通常用来表达集合中各个部分的百分比；
# pie函数可用来绘制饼状图；
# 详细信息及示例：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html
#
# ### 保存文件
# matplotlib.pyplot.savefig：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html
