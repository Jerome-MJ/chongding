#-*- coding: UTF-8 -*-
# import numpy as np

from PIL import ImageGrab,Image
import time
import os
PATH = lambda p: os.path.abspath(p)



def cap():
    # 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
    path=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    debug = False
    img = ImageGrab.grab(bbox=(100, 290, 950, 1000))
    img.save(path+".png")
    return path+".png"
    #img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)


def screenshot():
    path = PATH(os.getcwd() + "/screenshot")
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
        os.makedirs(path)
    cur_path=path + "/" + timestamp + ".png";
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(cur_path))
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    img= Image.open(cur_path)
    region = (0, 0, 800, 1000)
    # 裁切图片
    cropImg = img.crop(region)
    # 保存裁切后的图片
    cropImg.save("temp.png")
    return True
#end = time.time()
#print(end - beg)