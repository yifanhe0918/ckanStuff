##### A script that grab a dataset on bjdata.gov according to the specified dataset id, and import it into CKAN


import urllib2
import json
import ckanapi


class BjdataToCKAN:


    def __init__(self):
        #### id found on file info page
        self.id = 0
        #### key found in account info page
        self.key = 1506333154690
        self.orangeProxy = {'http': '10.193.250.16:8080'}
        self.url = ""
        self.name = ""
        # self.saveName = ""
        # self.extension = ""


    ####### Get file url from bjdata.gov
    def getFileUrl(self,id):
        self.id = id
        myUrl = "http://www.bjdata.gov.cn:80/cms/web/APIInterface/userApply.jsp?id=" + str(self.id) + "&key=" + str(self.key)
        # print myUrl
        proxy = urllib2.ProxyHandler(self.orangeProxy)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        req = urllib2.Request(myUrl)
        print req
        # print myUrl
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        # print myPage
        result = json.loads(myPage)["result"]
        self.url = result["address"]
        # self.extension = self.address.split(".")[-1]
        self.name = result["name"]
        print "file id: "+ str(self.id)
        print "file url: "+ str(self.url)
        print "file name: "+ self.name
        print " "
        return self.url

    ####### Check if the dataset exist. If yes, upload the resource to the current dataset; if not, create a dateset and upload the resource to it.
    def getFileAndUploadToCKAN(self,id,dsname,dstitle,rsname):
        url = self.getFileUrl(id)
        # print type(url)
        # saveAsName = self.name+"."+self.extension
        # print saveAsName
        ua = 'testUa'
        myCkan = ckanapi.RemoteCKAN('http://192.168.12.207:8020', apikey='d8fc8202-2f29-45fd-8fe6-0c63283dcd27', user_agent=ua)
        try:
            myCkan.action.package_create(name=dsname, title=dstitle)
            print "Created a new dataset: "
        except ckanapi.errors.ValidationError:
            print "Dataset already exists. Upload file to current datast: "
        result = myCkan.action.package_show(id=dsname)
        print result
        myCkan.action.resource_create(package_id=dsname, name=rsname, description=self.name,url=url)





##### to be filled

#### file id on bjdata.gov
idToDownload = 792588696
# idToDownload = 788140630

#### the name of dataset to upload the resource
datasetName = 'dataset_name333'

#### the title of the dataset to upload resource
datasetTitle = 'dataset_title444'

#### the resource name
resourceName = 'resource4'
# resourceName = 'resource2'



test1 = BjdataToCKAN()
test1.getFileAndUploadToCKAN(idToDownload,datasetName,datasetTitle,resourceName)