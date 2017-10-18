import ckanapi

myCkan = ckanapi.RemoteCKAN('http://192.168.12.207:8020', apikey='d8fc8202-2f29-45fd-8fe6-0c63283dcd27')
#
#### Create dataset
# createDataset = myCkan.action.package_create(
#     name='dataset_name4',
#     title='dataset_title',
    # tags=[{"name": "my_tag"}, {"name": "my-other-tag"}],
    # owner_org='test_org',
    # groups=[{"name":"test_group"}],
    # license_id="test_license_id",
    # )


# Get dataset
# result = myCkan.action.package_show(id="dataset_name333")
# id = result['id']
# # print result
# resource = result['resources']
# for i in resource:
#     print i
# print resource[0]['id']


## Get resource
# result = myCkan.action.resource_show(id="0000000000000")
# print result


# Upload resource
# uploadResource = myCkan.action.resource_create(
#     package_id="dataset_name",
#     name="resource",
#     description="this is a description",
#     format="csv",
#     upload=open('/Users/YifanHe/Desktop/yfhe3.txt', 'rb')
# )


####Update resource
# updateResource = myCkan.action.resource_update(
#     id ='000000000',
#     name = 'resource2',
#     upload=open('/Path/Of/The/File/test2.csv', 'rb'))


#### Get organization list
# print myCkan.action.organization_list()


# #### Get license list
# print myCkan.action.license_list()[0]
# print myCkan.action.license_list()[4]
# print len(myCkan.action.license_list())

### Get user
result = myCkan.action.user_show(id='yifanhe0918',include_datasets=True)

#####Update dataset's info
# updatePackage = myCkan.action.package_patch(
#     id="dataset_name",
#     # tags=[{"name": "my_tag"}, {"name": "my-other-tag"}],
#     # owner_org='test_org',
#     # groups=[{"name":"test_group"}],
#     license_id="test_license_id"
# )


##### Get tag info and its datasets
# result = myCkan.action.tag_show(id="my_tag",include_datasets=True)
# print result


##### Update dataset's organization


##### Update dataset's group


###### Update dataset's format


###### Update dataset's license





###### Search with filter
# print myCkan.action.package_search(q="Beijing",fq="groups:test_group")


###### Delete/Purge dataset
# myCkan.action.package_delete(id='dataset_name')
# myCkan.action.dataset_purge(id='dataset_name')


