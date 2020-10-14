'''
题目：从skimage.data模块中读取coffee、astronaut、chelsea三张图片，从本地读取一张sea图片，
显示在一个窗口中，将窗口划分成3行2列，分别用于显示这四张图片以及coffee和chelsea的灰度图像，
然后将coffee和chelsea的灰度图像保存到本地，保存为gif格式。
'''
from skimage import io, data, data_dir
import matplotlib.pyplot as plt

img1 = data.coffee()
img2 = data.astronaut()
img3 = data.chelsea()
img4 = io.imread('E:/sea.jpg')
img1_gray = io.imread(data_dir + '/coffee.png', as_gray=True)
img3_gray = io.imread(data_dir + '/chelsea.png', as_gray=True)

plt.subplot(3, 2, 1)        #将窗口分为三行两列六个子图，则可显示六幅图片
plt.title('coffee')         #第一幅图片标题
plt.imshow(img1)            #绘制第一幅图片

plt.subplot(3, 2, 2)
plt.title('astronaut')
plt.imshow(img2)
plt.axis('off')

plt.subplot(3, 2, 3)
plt.title('chelsea')
plt.imshow(img3)
plt.axis('off')

plt.subplot(3, 2, 4)
plt.title('sea')
plt.imshow(img4)
plt.axis('off')

plt.subplot(3, 2, 5)
plt.title('coffee_gray')
plt.imshow(img1[:,:,1], plt.cm.gray)
plt.axis('off')

plt.subplot(3, 2, 6)
plt.title('chelsea_gray')
plt.imshow(img3[:,:,1], plt.cm.gray)
plt.axis('off')
plt.show()


io.imsave('E:/coffee_gray.gif', img1_gray)
io.imsave('E:/chelsea_gray.gif', img3_gray)