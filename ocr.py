# -*- coding: utf-8 -*-

import urllib
import base64

#获取accessToken
def getAccessToken():
    apiKey = 'lWOW6OREaHyZrPkPbif30XUm'
    secretKey = 'SGKajZ5t9AMWpQZunatK4nr4b6muEzle'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + apiKey + '&client_secret=' + secretKey
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    #转换为字符串
    if (content):
        return eval(bytes.decode(content))['access_token']

#获取文字结果
def getResult(fileName):
    accessToken = getAccessToken()
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + accessToken

    #二进制方式打开图文件
    f = open(fileName, 'rb')
    #参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {'image': img}
    params = urllib.parse.urlencode(params).encode(encoding='UTF8')
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    content_result=eval(bytes.decode(content))["words_result"]
    #转换为字符串
    if (content):
        return content_result
