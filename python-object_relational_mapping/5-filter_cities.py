"""
A script that takes in the name of 
a state as an argument and lists all cities of that state, using the database 
"""

import MySQLdb
import sys

conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], 
                       passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = conn.cursor()
cur.execute(("SELECT cities.name FROM cities join states on'"+
             "'cities.state_id=states.id'"+
             "'WHERE states.name = %s ORDER BY cities.id ASC "),
             (sys.argv[4],))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()