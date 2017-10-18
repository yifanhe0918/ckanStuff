import datetime
import os
import sched
import time

import bothInfoRetrieve


def write():
    now = datetime.datetime.now()
    fileName = country_name + city_name + str(now.year) + str(now.month) + str(now.day)
    filePath = "/Users/YifanHe/Desktop/"+fileName + '.txt'
    print filePath

    if os.path.exists(filePath):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    print append_write
    record = open(filePath, append_write)
    print record
    string1 = now.strftime("%Y-%m-%d %H:%M")

    string2 = bothInfoRetrieve.retrieveInfo(country_name, city_name)
    string_for_output2 = string2.encode('utf8', 'replace')
    content = string1 +": "+ string_for_output2

    print "content: " + content
    record.write(content+'\n')
    record.close()


def Timer():
    print "Wrting file..."
    write()
    s.enter(1, 1, Timer, ())


s = sched.scheduler(time.time, time.sleep)
country_name = "cn"
city_name = "beijing"
s.enter(1, 1, Timer, ())
s.run()

