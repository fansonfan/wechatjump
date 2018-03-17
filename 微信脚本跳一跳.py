import os
import PIL, numpy
import matplotlib.pyplot as plt

form
matplotlib.animation
import FuncAnimation
import time


def get_screen_image():
    os.system('adb shell screencap -p  /adcard/screen.png')  # 获取当前手机界面的手机截图
    os.system('adb pull /sdcard/screen.png')  # 下载当前这个截图到电脑当前文件夹下
    return numpy, array(PIL.Image, open('screen.png'))


def jump_to_next(point1, point2):  # 计算弦的长度
    x1, x2 = point1;
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance * 1.35)))


def on_click(event, coor=[]):  # 绑定的鼠标单击事件
    global need_update
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())
        need_update = True


def update_screen(frame):  # 更新图片
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        need_update = False


return axes_image,

figure = plt.figure()  # 创建一个空白的图像对象/创建一张图片
axes_image = plt.imshow(get_screen_image(), animated=True)  # 把获取的图片画在坐标轴上面
figure.canvas.mpl_connect('button_press_event', on_click)
ani = FuncAnimation(figure, update_screen, interval=50, blit=True)
plt.show()