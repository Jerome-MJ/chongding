#-*- coding: UTF-8 -*-
from urllib.parse import quote

import image_search
import time
import capture
import requests
import webbrowser
def start(path):
    start=time.time()
    result_dic = image_search.getResult(path)
    question = result_dic.get("question")
    answer = result_dic.get("answer")

    #url2 = "http://www.baidu.com/s?wd=" + question
    url = "http://www.baidu.com/s?wd=" + question
    url = quote(url, safe="/:?=")
    response=requests.get(url)
    content=response.text
    print(question)
    try:
        size = len(answer)
        for i in range(size):
            ans=answer[i]
            # if ans.isdigit():
            #     print("%s\t%d" % (ans, content.count(ans)))
            # else:
            print("%s\t%d" % (ans, content.count(ans)))
        print(time.time()-start)
    except:
        print("")
    return url

#截屏 获取地址
path=capture.cap()

# 开始识别
url=start(path)
webbrowser.open(url, new=0, autoraise=True)