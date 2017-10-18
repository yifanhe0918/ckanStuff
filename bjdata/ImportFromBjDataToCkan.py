import ConfigParser

import ckanapi

import BjDataObjects

config = ConfigParser.RawConfigParser()
config.read('config.ini')

fileName = config.get('Section1', 'filename')
server = config.get('Section1', 'server')
apiKey = config.get('Section1','apikey')

myCkan = ckanapi.RemoteCKAN(server, apikey=apiKey)



with open(fileName) as f:
    content = f.readlines()
    successCounter = 0
    failureCounter = 0
    failureList = []
    print '   '
    print '-----------------------------'
    print '   '
    for i in content:
        try:
            htmlId = i.split(',')[0]
            BjDataPackage = BjDataObjects.BjDataPackage(htmlId)
            name = 'bjdata' + str(htmlId)
            print 'Dataset Name:' + name
            BjDataPackage.updateFiles()
            print  ' '

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
                    successCounter = successCounter+1
                    # print '         '+str(result)
                except Exception as e:
                    print "Failed to update. Please check manually: "+str(e)
                    failureCounter = failureCounter + 1
                    failureList.append(i)


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
                    successCounter = successCounter + 1
                    # print '         '+str(result)
                except Exception as e:
                    print "Failed to create. Please check manually: " + str(e)
                    failureCounter = failureCounter + 1
                    failureList.append(i)

        except Exception as e:
            print "Failed to locate the data set. Please check manually: " + str(e)
            failureCounter = failureCounter + 1
            failureList.append(i)

        print '   '
        print '-----------------------------'

    print '-----------------------------'
    print '   '
    print 'Succeed: '+str(successCounter)+'/'+str(len(content))
    print 'Fail: '+str(failureCounter)+'/'+str(len(content))
    for k in failureList:
        print '      '+k