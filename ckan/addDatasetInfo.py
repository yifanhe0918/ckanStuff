import ckanapi

ua = 'testUa'

myCkan = ckanapi.RemoteCKAN('http://192.168.12.207:8020', apikey='d8fc8202-2f29-45fd-8fe6-0c63283dcd27', user_agent=ua)

#### Create dataset with info
#### http://docs.ckan.org/en/latest/api/index.html#ckan.logic.action.create.package_create
createDataset = myCkan.action.package_create(
    name='dataset_name4',
    title='dataset_title',
    tags=[{"name": "my_tag"}, {"name": "my-other-tag"}],
    owner_org='test_org',
    groups=[{"name":"test_group"}],
    license_id="test_license_id",
    )

##### Update current dataset's info
##### http://docs.ckan.org/en/latest/api/index.html#ckan.logic.action.update.package_update
updatePackage = myCkan.action.package_patch(
    id="dataset_name",
    tags=[{"name": "my_tag"}, {"name": "my-other-tag"}],
    owner_org='test_org',
    groups=[{"name":"test_group"}],
    license_id="test_license_id"
)

##### Upload resource with info
##### http://docs.ckan.org/en/latest/api/index.html#ckan.logic.action.create.resource_create
uploadResource = myCkan.action.resource_create(
    package_id="dataset_name",
    name="resource",
    description="this is a description",
    format="csv",
    upload=open('/Users/YifanHe/Desktop/yfhe3.txt', 'rb')
)
