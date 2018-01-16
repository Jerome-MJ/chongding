# 冲顶大会 and 百万英雄辅助

> 首先说耗时，基本都在2s之内，稳定点是1s左右。不依靠adb，减少截屏、传输文件、识别大图ocr的时间。
>
> 利用python 截取pc区域页面，利用百度识别对应问题，然后根据问题查询百度，匹配答案出现次数，仅仅只能作为辅助，因为我靠这个。还没有拿到过奖金。。被冷门知识难到了。
>
> 注意：
>
> 1. 问题中如果包含没有，或者不这样的意思选最少出现。因为百度查询一般都是查询出来的他有哪些作品。
>
>
> 2. 另外答案是数字类的就自己靠命运吧。 数字容易跟年份一类冲突，导致查询结果会有影响
> 3. 出现次数的时候仅供参考，尽量还是看一下浏览器内的相关信息。两者结合选、
> 4. 屏幕选好区域后，在百万英雄、芝士超人、冲顶大会都是可以用的，不需要二次修改屏幕区域。
> 5. 已在各平台收获几十元，感觉太浪费时间了。而且加入辅助，也不是所有问题都可以答对。大家就随意玩玩吧。

# 效果图

![](http://p1it9mdjq.bkt.clouddn.com/QQ20180111-0@2x.png)

### 新增:

  当文字识别完自动打开浏览器，百度查询相关问题。

### 工具：

1. 夜神模拟器（冲顶大会不行，百万英雄可以正常使用）

2. Chrome+Vysor投屏，这个教程可以高清破解。https://www.jianshu.com/p/66608ffebc31

3. 之前试过adb截图。。太慢了。。后来就没考虑用

   ​

### 依赖包

```python
#目前是基于PY3.6写的，2.7的基本也可以用，无非换一下网络层面的用urllib2就行。
# 在3.6用的urllib.request 太慢了，高达5s以上，requests都是1-2s内响应
pip install baidu-aip
pip install Pillow
pip install requests
```



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

