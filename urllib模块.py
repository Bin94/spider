import urllib.request  #导入模块
import urllib.parse

url = "http://www.baidu.com"
#抓取网页
file = urllib.request.urlopen(url)
#存储内容
data = file.read()
print(data)
dataline = file.readline()
print(dataline)
#写入文件
fhandle = open("./1.html","wb")
fhandle.write(data)
fhandle.close()

#利用urlretrieve直接写入文件
filename = urllib.request.urlretrieve(url,"./2.html")
urllib.request.urlcleanup()  #清除缓存

#获取页面信息
print(file.info()) #info信息
print(file.getcode()) #状态码
print(file.geturl())  #url

#对字符编码与解码
str = "ABC:EFG&"
#编码
str2 = urllib.request.quote(str)
#解码
str3 = urllib.request.unquote(str2)
print(str,str2,str3)

#在访问时403报错，采用修改User-Agent模拟浏览器访问
#第一种方式
#使用build_opener()修改User-Agent
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0")
opener = urllib.request.build_opener()  #创建opener对象
opener.addheaders = [headers]  #设置opener头信息
data = opener.open(url).read()  #使用opener打开链接

#第二种方式
#使用add_header()添加报头
req = urllib.request.Request(url)  #创建Request对象
#添加报头信息
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
data = urllib.request.urlopen(req).read()  #使用添加了报头信息的request对象访问


#超时设置
file = urllib.request.urlopen(url,timeout=1)  #timeout属性代表网站未在1秒内响应就判定为超时

#HTTP协议请求
#1、GET请求
keywd = "spider"
keywd_encode = urllib.request.quote(keywd) #若存在中文字符或特殊字符需要重新编码
keywd_url = "http://www.baidu.com/s?wd=" + keywd_encode
req = urllib.request.Request(keywd_url)
data = urllib.request.urlopen(req).read()
fhandle = open("./http_get.html","wb")
fhandle.write(data)
fhandle.close()

#2、POST请求
posturl = "http://www.iqianyue.com/mypost/"
postdata = {"name":"123",
            "pass":"456"}
postdata_encode = urllib.parse.urlencode(postdata).encode("utf-8")  #将数据设置为'utf-8'编码
req = urllib.request.Request(posturl,postdata_encode)
data = urllib.request.urlopen(req).read()
fhandle = open("./http_post.html","wb")
fhandle.write(data)
fhandle.close()

#代理服务器
#http://www.xicidaili.com/
proxy_addr = "123.57.84.116:8118"
proxy = urllib.request.ProxyHandler({'http':proxy_addr})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
data = urllib.request.urlopen(url).read()
fhandle = open("./proxy.html","wb")
fhandle.write(data)
fhandle.close()
