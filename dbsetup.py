import pymysql
import sys

try:

    con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratemybitches')
    with con:
        cur = con.cursor()
        cur.execute("DROP DATABASE IF EXISTS ratemybitches")
        cur.execute("CREATE DATABASE ratemybitches")
        # timestamp format: yyyy-mm-dd hh-mm-ss
        cur.execute("CREATE TABLE ratemybitches.img (id int(3) NOT NULL AUTO_INCREMENT, extension varchar(5) NOT NULL, time TIMESTAMP DEFAULT 0 NOT NULL, upvotes int(5) NOT NULL, KEY(id))") 
        # insert test data for interation with other applications/files
        cur.execute("INSERT INTO ratemybitches.img (id, extension, time, upvotes) VALUES (1, '.jpg', '2001-01-05 00:00:01', 100)")
        cur.execute("INSERT INTO ratemybitches.img (id, extension, time, upvotes) VALUES (2, '.gif', '2002-02-04 00:00:01', 200)")
        cur.execute("INSERT INTO ratemybitches.img (id, extension, time, upvotes) VALUES (3, '.png', '2003-03-03 00:00:01', 300)")
        cur.execute("INSERT INTO ratemybitches.img (id, extension, time, upvotes) VALUES (4, '.tif', '2004-04-02 00:00:01', 400)")
        cur.execute("INSERT INTO ratemybitches.img (id, extension, time, upvotes) VALUES (5, '.lol', '2005-05-01 00:00:01', 500)")

    # result = con.use_result()
    # print "MySQL version: %s" % \
    #     result.fetch_row()[0]
    
except pymysql.Error:
    print("Error!")
    sys.exit(1)

finally:
    if con:
        con.close()