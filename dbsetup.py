import pymysql
import sys

try:

    con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratemybitches')
    with con:
        cur = con.cursor()
        cur.execute("DROP DATABASE IF EXISTS ratemybitches")
        cur.execute("CREATE DATABASE ratemybitches")
        cur.execute("USE ratemybitches")
        # timestamp format: ss:mm:hh:dd:mm:yyyy
        cur.execute("CREATE TABLE img (id int(3) NOT NULL AUTO_INCREMENT, file_extension varchar(5) NOT NULL, time varchar(19) NOT NULL, upvotes int(5) NOT NULL, KEY(id))") 
        # insert test data for interation with other applications/files
        cur.execute("INSERT INTO ratemybitches.img (id, file_extension, time, upvotes) VALUES (1, '.jpg', '60:60:24:31:12:2000', 100)")

    # result = con.use_result()
    # print "MySQL version: %s" % \
    #     result.fetch_row()[0]
    
except pymysql.Error:
    print("Error!")
    sys.exit(1)

finally:
    if con:
        con.close()