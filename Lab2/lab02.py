'''
实验内容与要求
（1）编写和运行教材《数字图像处理与python实现》第1章P20~P25中的所有代码。
（2）裁剪skimage.data示例中coffee图片的第60列至倒数60列的部分，然后对裁剪后的图片随机添加椒盐噪声。
（3）对（2）裁剪后的图片分别进行gamma调整（gamma=1.5）和log对数调整，
并判断其对比度是否偏低，如果偏低则调整该图片的对比度。
（4）对（3）裁剪后的图片进行二值化，像素值大于180的变为1，否则变为0。
（5）将以上（2）、（3）、（4）中原图和处理后的图片在一个窗口中全部显示，并设置各子图标题。
'''


from skimage import io, data
import numpy as np
import matplotlib.pyplot as plt

img = data.coffee()

roi = img[:, 60:-61, :]
io.imshow(roi)
# io.imshow(img)
plt.show()

'''
# 随机生成5000个椒盐
rows, cols, dims = img.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255
io.imshow(img)
plt.show()
'''














