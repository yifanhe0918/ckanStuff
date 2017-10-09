import urllib2
import json
import re

class BjDataFile():
    def __init__(self,name,format,date,downloadId,url):
        self.name = name
        self.format = format
        self.date = date
        self.downloadId = downloadId
        self.url = url


class BjDataPackage():

    def __init__(self,htmlId):
        self.htmlId = htmlId
        self.fileNum = 0
        self.fileList =[]
        self.title = ''

    def updateFiles(self):
        orangeProxy = {'http': '10.193.250.16:8080'}
        proxy = urllib2.ProxyHandler(orangeProxy)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

        myUrl1 = 'http://www.bjdata.gov.cn/cms/web/APIInterface/dataDoc.jsp?contentID='+str(self.htmlId)
        req1 = urllib2.Request(myUrl1)
        myResponse1 = urllib2.urlopen(req1)
        myPage1 = myResponse1.read()
        # print myPage1
        entry = re.findall('<p  class="tab-title">(.*?)</table>', myPage1,re.S)
        sourceListRaw = re.findall('<td>(.*?)</tr>\r\n\t', entry[0],re.S)
        self.fileNum = len(sourceListRaw)+1
        self.fileList = []
        for i in sourceListRaw:
            # print i
            infos = i.split('</td>')
            name = infos[0]
            format = infos[1].split('>')[1]
            date = infos[2].split('>')[1]
            downloadId = infos[3].split('>')[1]
            key = 1506333154690
            url = "http://www.bjdata.gov.cn:80/cms/web/APIInterface/userApply.jsp?id=" + str(downloadId) + "&key=" + str(key)
            req2 = urllib2.Request(url)
            myResponse2 = urllib2.urlopen(req2)
            myPage2 = myResponse2.read()
            result = json.loads(myPage2)["result"]
            self.url = result["address"]
            print name,format,date,downloadId,url
            dataFile = BjDataFile(name,format,date,downloadId,url)
            self.fileList.append(dataFile)
        self.title = self.fileList[0].name


