#-*- coding: UTF-8 -*-
from aip import AipOcr

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 你的 APPID AK SK """
APP_ID = '自行申请appid'
API_KEY = '自行申请api key'
SECRET_KEY = '自行申请secret_key'


def getResult(filename):
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    image = get_file_content(filename)

    """ 调用通用文字识别, 图片参数为本地图片 """
    result=client.basicGeneral(image)
    # result="{u'log_id': 578283474979346368, u'words_result_num': 9, u'words_result': [{u'words': u'\u6253\u65b0\u7684\u6807\u7b7e\u9875\u9996\u9875\u25a1\u516c\u53f8\u25a1RN\u25a1\u5b66\u4e60\u7f51\u7ad9\u25a1\u90e8\u7f72Qb'}, {u'words': u'\u4e3a\u82f1\u8bed\u538c'}, {u'words': u'\u76f2\u76ee\u81ea\u4fe1\u7fa4'}, {u'words': u'\u5f90\u5176\u4e1c'}, {u'words': u'2'}, {u'words': u'\u5468\u51e1:\u60f3\u4f4f\u8fd9\u6837\u4e00\u4e2a\u5c0f\u623f\u5b50\u662f\u591a'}, {u'words': u'3'}, {u'words': u'6. Studio Android Studio a##'}, {u'words': u'\u5e1d\u90fd-\u7f8e\u6ecbhttp:// www.apkbu'}]}"
    count=result.get("words_result_num")
    result_dic={"answer":None,"question":""}
    if count>3:
        answers=result.get("words_result")
        s=""
        ques_len=count
        ans_index=2
        for i in range(ques_len):
            words=answers[i].get("words")
            s+=words
            if words.find("?")>=0:
                ans_index=i+1
                break
        new_ans=answers[ans_index:]
        new_ans2=list()
        for i in range(len(new_ans)):
            new_ans2.append(new_ans[i].get("words"))
        result_dic["question"]=s
        result_dic["answer"]=new_ans2
    return result_dic
