import pymysql
import sys

# only necessary when testing user login shit
import bcrypt

try:

    con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratethis')
    with con:
        cur = con.cursor()
        cur.execute("DROP DATABASE IF EXISTS ratethis")
        cur.execute("CREATE DATABASE ratethis")
        cur.execute("USE ratethis")
        # timestamp format: yyyy-mm-dd hh-mm-ss
        cur.execute("CREATE TABLE img (id int(3) NOT NULL AUTO_INCREMENT, extension varchar(5) NOT NULL, time TIMESTAMP DEFAULT 0 NOT NULL, upvotes int(5) NOT NULL, KEY(id))")
        cur.execute("CREATE TABLE users (id int(3) NOT NULL AUTO_INCREMENT, username varchar(20) NOT NULL, password varchar(60), KEY(id))")
        
        # insert test data
        '''
        cur.execute("INSERT INTO img (id, extension, time, upvotes) VALUES (1, '.jpg', '2001-01-05 00:00:01', 100)")
        cur.execute("INSERT INTO img (id, extension, time, upvotes) VALUES (2, '.gif', '2002-02-04 00:00:01', 200)")
        cur.execute("INSERT INTO img (id, extension, time, upvotes) VALUES (3, '.png', '2003-03-03 00:00:01', 300)")
        cur.execute("INSERT INTO img (id, extension, time, upvotes) VALUES (4, '.tif', '2004-04-02 00:00:01', 400)")
        cur.execute("INSERT INTO img (id, extension, time, upvotes) VALUES (5, '.lol', '2005-05-01 00:00:01', 500)")
        '''

        cur.execute("INSERT INTO users (id, username, password) VALUES (1, 'nicosogangstar', \'" + bcrypt.hashpw('password123',    bcrypt.gensalt()) + "\')")
        cur.execute("INSERT INTO users (id, username, password) VALUES (2, 'Maxinary',       \'" + bcrypt.hashpw('secretpassword', bcrypt.gensalt()) + "\')")
    
except pymysql.Error as e:
    print("You have an error in your SQL syntax:\n" + str(e.args))
    sys.exit(1)

finally:
    if con:
        con.close()