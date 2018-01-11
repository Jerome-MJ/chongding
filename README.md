# 冲顶大会 and 百万英雄辅助

> 利用python 截取pc区域页面，利用百度识别对应问题，然后根据问题查询百度，匹配答案出现次数，仅仅只能作为辅助，因为我靠这个。还没有拿到过奖金。。被冷门知识难到了。



### 工具：

1. 夜神模拟器（冲顶大会不行，百万英雄可以正常使用）

2. Chrome+Vysor投屏，这个教程可以高清破解。https://www.jianshu.com/p/66608ffebc31

3. 之前试过adb截图。。太慢了。。后来就没考虑用

   ​

### 步骤

1. 修改capture.py文件下的cap中bbox的范围

   ```python
   img = ImageGrab.grab(bbox=(100, 290, 950, 1000)) #参数依次为x，y，宽，高，一般把视频放在左边顶上容易调整
   ```

2. 修改image_search.py 中的APP_IP等参数

   ```python
   """ 你的 APPID AK SK """
   APP_ID = '自行申请appid'
   API_KEY = '自行申请api key'
   SECRET_KEY = '自行申请secret_key'
   ```

   ​

3. 启动Search.py，运行调试截图的时候可以将start方法注释，节省api次数

   ```python

   #截屏 获取地址
   path=capture.cap()
   # 开始识别
   start(path)
   ```

![图像1](https://github.com/Jerome-MJ/chongding/raw/master/2018-01-11 17:09:40.png)