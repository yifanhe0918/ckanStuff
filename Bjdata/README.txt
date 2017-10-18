This is a tool that transfer the data from http://www.bjdata.gov.cn/ to CKAN database.
The tool is based on ckanapi. Please install ckanapi before running this tool. Installation see https://github.com/ckan/ckanapi

Please edit config.ini file to edit configuration before using:

server: the server where CKAN is located at. Default: http://192.168.12.207:8020
apikey: To find your API key, login to the CKAN site using its web interface and visit your user profile page.
filename: the full path of a txt file that contains the summary of data set IDs.
          An ID is the last part (the number part) of the path of the webpage url.
          Each line is a single entery of dataset, format as: ID, Filename
          Example:

                  The data sets we would like to import:
                        http://www.bjdata.gov.cn/zyml/ajg/slyw/8658.htm
                        http://www.bjdata.gov.cn/zyml/ajg/slyw/6785.htm
                        http://www.bjdata.gov.cn/zyml/ajg/slyw/8574.htm
                        http://www.bjdata.gov.cn/zyml/ajg/slyw/10918.htm

                  Format in txt file:
                        8658,北京市软件产品检测机构认可名单
                        6785,公路气象数据
                        8574,北京市旅游景区游览舒适度指数
                        10918,演出场所经营单位

Run ImportFromBjDataToCkan.py to start importing.
If the data set does not exist, create a new one. If the data set already exists, update the content.