import BjDataObjects
import ckanapi

fileName = '/Users/YifanHe/Desktop/toImport.txt'

ua = 'testUa'
myCkan = ckanapi.RemoteCKAN('http://192.168.12.207:8020', apikey='d8fc8202-2f29-45fd-8fe6-0c63283dcd27', user_agent=ua)

with open(fileName) as f:
    content = f.readlines()
    for i in content:
        htmlId = i.split(',')[0]
        BjDataPackage = BjDataObjects.BjDataPackage(htmlId)
        BjDataPackage.updateFiles()

        name = 'bjdata' + str(htmlId)
        print 'Dataset Name:' + name
        try:
            result = myCkan.action.package_show(id=name)
            print "Dataset already exists. Checking Updates... "
            package_id = result['id']
            resource = result['resources']
            try:
                for i in resource:
                    rsId = i['id']
                    myCkan.action.resource_delete(id = rsId)
                for j in BjDataPackage.fileList:
                    myCkan.action.resource_create(package_id = package_id,
                                                  name = j.name + '.'+j.format,
                                                  description="last update: " + j.date,
                                                  format=j.format)
                print "Succeeded!"
                print result
            except:
                print "Failed to update. Please check manually."

        except ckanapi.errors.NotFound:
            print "Does not Exist. Creating a new dataset... "
            try:
                myCkan.action.package_create(name=name, title=BjDataPackage.title)
                result = myCkan.action.package_show(id=name)
                package_id = result['id']
                for j in BjDataPackage.fileList:
                    myCkan.action.resource_create(package_id = package_id,
                                                  name = j.name +'.'+ j.format,
                                                  description="last update: " + j.date,
                                                  format=j.format)
                print "Succeeded!"
                print result
            except:
                print "Failed to create. Please check manually."