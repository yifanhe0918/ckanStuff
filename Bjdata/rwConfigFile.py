import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('Section1')
config.set('Section1', 'server', 'http://192.168.12.207:8020')
config.set('Section1', 'apiKey', 'd8fc8202-2f29-45fd-8fe6-0c63283dcd27')
config.set('Section1', 'fileName', '/Users/YifanHe/PycharmProjects/ckan_weatherAndBjdata/Bjdata/datasetList.txt')


with open('config.ini', 'wb') as configfile:
    config.write(configfile)