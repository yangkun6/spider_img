#coding:utf-8
from lxml import etree
import urllib
import urllib2
import time

"""
#爬单页，目标
url = "https://www.qiushibaike.com/pic/"
header={
    "Referer":"https://www.qiushibaike.com/",#爬的来源
    #User-Agent模拟浏览器
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
req = urllib2.Request(url=url,headers=header)
response = urllib2.urlopen(req)#py2爬取
content = response.read()
html = etree.HTML(content)#lxml转html
img_list = html.xpath("//img")#//匹配所有
# print  img_list
for img in img_list:#.text文本 .attrib属性 .tag标签
    attrib = img.attrib
    if attrib.get("alt"):
        name = attrib.get("alt")
        src = "http:"+attrib["src"]
        if "JPEG" in src:
            name += ".JPEG"
        elif "jpg" in src:
            name += ".jpg"
        else:
            name += ".png"
        path = "C:\\Users\\Administrator\\Desktop\\img\\"+name
        try:
            urllib.urlretrieve(src,path)#要用urllib才行
        except:
            pass
        else:
            print("%s is down"%name)
            time.sleep(1)#不能给服务器照压
"""

#爬取多页
def getPage(url,up_url):
    header = {
        "Referer":"up_url",#来源
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    request = urllib2.Request(url=url,headers=header)
    respose = urllib2.urlopen(request)
    content = respose.read()
    html = etree.HTML(content)
    img_list = html.xpath("//img")
    for img in img_list:
        attrib = img.attrib
        if attrib.get("alt"):
            name = attrib.get("alt")
            src = "http:"+attrib["src"]
            if "JPEG" in src:
                name += ".JPEG"
            elif "jpg" in src:
                name +=".jpg"
            else:
                name += ".png"
            path = "D:\\img\\"+name
            try:
                urllib.urlretrieve(src,path)
            except:
                pass
            else:
                print ("%s is down"%name)
                time.sleep(1)
def main():
    for page in range(1,36):
        up_url = page-1
        if page == 1:#第一页
            url = "https://www.qiushibaike.com/pic/"
            up_url ="https://www.qiushibaike.com/"
        else:#其他页
            url = "https://www.qiushibaike.com/pic/page/%d/?s=5076950"%page
            up_url = "https://www.qiushibaike.com/pic/page/%d/?s=5076950"%up_url
        getPage(url,up_url)#调用爬
        time.sleep(3)#下页停3秒不能给服务器照压
if __name__ == '__main__':
    main()

