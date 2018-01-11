#-*- coding: UTF-8 -*-
import urllib.request
from urllib.parse import quote

import image_search
import time
import capture
import requests


def start(path):
    start=time.time()
    result_dic = image_search.getResult(path)
    question = result_dic.get("question")
    answer = result_dic.get("answer")

    url = "http://m.baidu.com/s?wd=" + question
    url = quote(url, safe="/:?=")
    response=requests.get(url)
    content=response.text
    # result = urllib.request.urlopen(url)
    # content = result.read()
    # content = content.decode("utf-8")
    print(question)
    size = len(answer)
    for i in range(size):
        print("%s\t%d" % (answer[i], content.count(answer[i])))
    print(time.time()-start)


#截屏 获取地址
path=capture.cap()

# 开始识别
start(path)



