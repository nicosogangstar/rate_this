import pymysql

con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratemybitches')

start = 3
start-=1
end = 5
column = 3


with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM img LIMIT " + str(start) + "," + str(end))
    
    rows = cur.fetchmany(size=(end-start))
    for row in rows:
    	print(row[column])

cur.close()
con.close()