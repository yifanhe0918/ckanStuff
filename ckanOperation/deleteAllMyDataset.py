import ckanapi
myCkan = ckanapi.RemoteCKAN('http://192.168.12.207:8020', apikey='d8fc8202-2f29-45fd-8fe6-0c63283dcd27')
result = myCkan.action.user_show(id='yifanhe0918',include_datasets=True)
num=0
for i in result['datasets']:
    num = num+1
    print i['title']
    id = i['id']
    myCkan.action.dataset_purge(id=id)
print 'Successfully deleted '+str(num)+ ' datasets'