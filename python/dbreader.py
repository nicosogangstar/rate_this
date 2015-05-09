import pymysql

def fetch_data(strcolumn = 'id', start=1, end=1):
	con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratemybitches')
	start-=1
	result = ''
	if strcolumn=='id':
		column = 0

	elif strcolumn=='extention':
		column = 1

	elif strcolumn=='timestamp':
		column = 2

	elif strcolumn=='upvotes':
		column = 3

	with con:
	    cur = con.cursor()
	    cur.execute("SELECT * FROM img LIMIT " + str(start) + "," + str(end))
	    
	    rows = cur.fetchmany(size=(end-start))
	    for row in rows:
	    	result = result + str(row[column]) + ", "
	cur.close()
	con.close()
	return result[0:-2]

print(fetch_data('id', 1, 2))