# BiliSpider
利用Bilispider，轻松下载B站视频！
bili-spider-src 是源代码文件，只供调试使用
## 工作原理介绍
很简单，就是通过发送安卓的UA获取到B站视频的源地址，然后用urllib.request Moudel发送请求下载下来（用正则匹配）。保存到程序所在的目录下。
### 稳定性
夏荷确定该软件稳定性较高，不过用的人太多太多可能会玩脱。相较于其它软件来说，优势是……我们这个是直接获取源地址的，从m.bilibili.com上的Js代码里面获取URL地址，然后下载。
仅仅21行代码
