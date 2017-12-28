import pymysql
import pymysql.cursors
from prettytable import PrettyTable

conn = pymysql.connect(	host="localhost",
						user="root",
						passwd="secret",
						db="eve_test")
						
cursor = conn.cursor()

cursor.execute("SELECT typeName from invtypes WHERE groupID = 85;")
print(cursor.description)
print()

rows = cursor.fetchall()

table = [item[0] for item in rows]

pt = PrettyTable(["Item Name"])
for row in table:
	pt.add_row([row])
print(pt)

cursor.close()
conn.close()