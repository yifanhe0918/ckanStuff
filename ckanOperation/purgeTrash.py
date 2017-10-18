import urllib2

admin_api_key = 'd8fc8202-2f29-45fd-8fe6-0c63283dcd27'
ckan_base = 'http://192.168.12.207:8020'

request = urllib2.Request('{0}/ckan-admin/trash'.format(ckan_base))
request.add_header('Authorization', admin_api_key)
response = urllib2.urlopen(request, 'purge-packages=purge')
assert response.code == 200