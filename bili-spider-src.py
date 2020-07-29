import re
import urllib.request
def download1(url):
    headers={"User-Agent" : "Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36"}  #header 字典形式
    #选择代码  ctrl + 鼠标左键 查看变量或者函数或者类的定义
    request=urllib.request.Request(url,headers=headers)   # 发送请求
    #也可以通过调用Request.add_header()  添加/修改一个特定的  header
    request.add_header("Connection","keep-alive")  #一直活着
    response=urllib.request.urlopen(request)  #打开请求
    data=response.read()    #读取数据
    print(response.code)    #可以查看相应状态码
    return data
bvid = "BV1TZ4y1x7yU"#这里面输入BV号，"BV"要求大写！BV号要求区分大小写！
url="https://m.bilibili.com/video/" + bvid
html = download1(url).decode("utf-8")
video_uri = re.findall("readyVideoUrl: '(.+)',", html)
video_uri = 'http:' + video_uri[0]
video_file = download1(video_uri)
video_name = bvid + ".mp4"
f = open(video_name,"wb")
f.write(video_file)