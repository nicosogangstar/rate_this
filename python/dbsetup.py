import _mysql
import sys

try:
    con = _mysql.connect('localhost', 'root', 'iloveyeeting', 'ratemybitches')
        
    con.query("DROP DATABASE IF EXISTS ratemybitches")
    con.query("CREATE DATABASE ratemybitches")
    con.query("USE ratemybitches")
    # timestamp format: ss:mm:hh:dd:mm:yyyy
    con.query("CREATE TABLE img (id int(3) NOT NULL AUTO_INCREMENT, file_extension varchar(5) NOT NULL, time varchar(19) NOT NULL, upvotes int(5) NOT NULL, KEY(id))") 
    # insert test data for interation with other applications/files
    con.query("INSERT INTO ratemybitches.img (id, file_extension, time, upvotes) VALUES (1, '.jpg', '60:60:24:31:12:2000', 100)")

    # result = con.use_result()
    # print "MySQL version: %s" % \
    #     result.fetch_row()[0]
    
except _mysql.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()