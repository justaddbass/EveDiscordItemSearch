import pymysql
import pymysql.cursors

conn = pymysql.connect(	host="localhost",
							user="root",
							passwd="secret",
							db="eve_test")
							
cursor = conn.cursor()
	
def close():
	cursor.close()
	conn.close()

def getItemsInCategory(category=''):
	if category == '':
		cursor.execute('SELECT marketGroupName FROM invmarketgroups WHERE parentGroupID IS NULL;')
	else:
		cursor.execute('SELECT marketGroupName FROM invmarketgroups WHERE marketGroupID IN (SELECT parentGroupID FROM invmarketgroups WHERE marketGroupName = "%s")',category)
	rows = cursor.fetchall()
	table = [item[0] for item in rows]
	return '\n'.join(table)

#cursor.execute("SELECT typeName from invtypes WHERE groupID = 85;")
#print(cursor.description)
#print()

#rows = cursor.fetchall()

#table = [item[0] for item in rows]

#pt = PrettyTable(["Item Name"])
#for row in table:
#	pt.add_row([row])
#print(pt)
