# coding=utf-8
import matplotlib.pyplot
import numpy  # 科学计算库

data = numpy.arange(100, 201)  # 利用NumPy生成一个[100, 200]之间的整数数组
# data = range(100, 201)  # 利用内置函数range生成整数数组，效果与上一句相同
matplotlib.pyplot.plot(data)  # 绘制图形，这里data作为图形纵坐标（y轴），matplotlib默认设置了图形横坐标（x轴）
matplotlib.pyplot.show()  # 显示图形

# ### Matplotlib
# HomePage : https://matplotlib.org/
# Python语言的绘图库，功能强大，可绘制出各种专业的图像，支持各种平台，可实现定制；
#
# ### 文档信息
#   - Docs : https://matplotlib.org/contents.html
#   - Examples：https://matplotlib.org/gallery/index.html
#   - Tutorials：https://matplotlib.org/tutorials/index.html
#   - API：https://matplotlib.org/api/
#   - User Guide：https://matplotlib.org/contents.html
#   - Function Indexing：https://matplotlib.org/genindex.html
#   - Python Module Index：https://matplotlib.org/py-modindex.html
