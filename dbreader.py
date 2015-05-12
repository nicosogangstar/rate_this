import pymysql
import bcrypt
#
#
# retrieving data(more specifically, post info)
#
#

def fetch_data(strcolumn = 'id', start=1, end=1):
    con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratethis')
    result = ''
    with con:
        cur = con.cursor()

        if strcolumn=='id':
            start-=1
            cur.execute("SELECT id, extension FROM img LIMIT " + str(start) + "," + str(end))
            rows = cur.fetchmany(size=(end-start))
            for row in rows:
                result = result + str(row[0]) + row[1] + " "

        elif strcolumn=='timestamp':
            cur.execute("SELECT id, extension FROM img WHERE time BETWEEN \'" + start + "\' AND \'" + end + "\'")
            rows = (cur.fetchall())
            for row in rows:
                result = result + str(row[0]) + row[1] + " "

        elif strcolumn=='upvotes':
            cur.execute("SELECT id, extension FROM img WHERE upvotes BETWEEN " + str(start) + " AND " + str(end))
            rows = (cur.fetchall())
            for row in rows:
                result = result + str(row[0]) + row[1] + " "

    cur.close()
    con.close()
    return result[0:-1].split()

#
#
# password verification!
#
#

def check_password(username='', password=''):
    if username!='' and password!='':
        con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratethis')
        
        with con:
            cur = con.cursor()
            cur.execute("SELECT password FROM users WHERE username=\'" + username + "\'")
            hashed = cur.fetchone()[0]
    cur.close()
    con.close()

    if bcrypt.hashpw(password, hashed) == hashed:
        return True
    else:
        return False
        

# print(fetch_data('timestamp', '2000-03-26 00:00:01', '2003-03-26 00:00:01'))
# print(fetch_data('id', 3, 5))
# print(fetch_data('upvotes', 200, 500))
