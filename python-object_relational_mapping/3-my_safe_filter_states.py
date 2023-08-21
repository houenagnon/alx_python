"""A  script that takes in an argument and displays all values in the 
states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = conn.cursor()
query = "SELECT * FROM states WHERE name ='"+ sys.argv[4] + "'ORDER BY id ASC "
cur.execute(query)
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()