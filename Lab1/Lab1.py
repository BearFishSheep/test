# '''
# 题目：从skimage.data模块中读取coffee、astronaut、chelsea三张图片，从本地读取一张sea图片，
# 显示在一个窗口中，将窗口划分成3行2列，分别用于显示这四张图片以及coffee和chelsea的灰度图像，
# 然后将coffee和chelsea的灰度图像保存到本地，保存为gif格式。
# '''
#
# from skimage import io, data
# import matplotlib.pyplot as plt
#
# img1 = data.coffee()
# img2 = data.astronaut()
# img3 = data.chelsea()
# img4 = io.imread('E:/sea.jpg')
# img1_gray = io.imread(data_dir+'/coffee.png', as_gray=True)
# img3_gray = io.imread(data_dir+'/chelsea.png', as_gray=True)
#
# plt.subplot(3, 2, 1)        #将窗口分为三行两列六个子图，则可显示六幅图片
# plt.title('coffee')         #第一幅图片标题
# plt.imshow(img1)            #绘制第一幅图片
#
# plt.subplot(3, 2, 2)
# plt.title('astronaut')
# plt.imshow(img2)
# plt.axis('off')
#
# plt.subplot(3, 2, 3)
# plt.title('chelsea')
# plt.imshow(img3)
# plt.axis('off')
#
# plt.subplot(3, 2, 4)
# plt.title('sea')
# plt.imshow(img4)
# plt.axis('off')
#
# plt.subplot(3, 2, 5)
# plt.title('coffee_gray')
# plt.imshow(img1[:,:,1], plt.cm.gray)
# plt.axis('off')
#
# plt.subplot(3, 2, 6)
# plt.title('chelsea_gray')
# plt.imshow(img3[:,:,1], plt.cm.gray)
# plt.axis('off')
# plt.show()
#
#
# io.imsave('E:/coffee_gray.gif', img1[:,:,1])
# io.imsave('E:/chelsea_gray.gif', img3[:,:,1])
#
#
#
#
# '''
# ## 1.从外部读取图片并显示
# from skimage import io
# from matplotlib import pyplot as plt
#
# # pic = io.imread('E:/dog.jpg')
# pic = io.imread('E:/dog.jpg', as_gray=True)   # 读取灰度图像
# io.imshow(pic)
# plt.show()
# '''
#
# '''
# ## 2.skimage.data自带图片
# from skimage import io, data, data_dir
# from matplotlib import pyplot as plt
#
# pic = data.chelsea()
# # pic = data.moon()
# print(data_dir)
# io.imshow(pic)
# plt.show()
# '''
#
# '''
# ## 3.保存图片
# from skimage import io, data
# from matplotlib import pyplot as plt
#
# pic = data.chelsea()
# io.imshow(pic)
# io.imsave('E:/cat.jpg', pic)
# plt.show()
# '''
#
# '''
# ## 4.图片信息获取
# from skimage import io, data
# from matplotlib import pyplot as plt
#
# img = data.chelsea()
# io.imshow(img)
# plt.show()
#
# print(type(img))        #显示类型
# print(img.shape)        #显示尺寸
# print(img.shape[0])     #图片高度
# print(img.shape[1])     #图片宽度
# print(img.shape[2])     #图片通道数
# print(img.size)         #显示总像素个数
# print(img.max())        #最大像素值
# print(img.min())        #最小像素值
# print(img.mean())       #像素平均值
# '''
#
# '''
# ## 5.matplotlib显示图像
# import matplotlib.pyplot as plt
# from skimage import io, data
#
# img = data.astronaut()
# plt.imshow(img)
# plt.show()
# '''
#
# ## 6.用figure函数和subplot函数分别创建主窗口与子图
#
#
#
#
