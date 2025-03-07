#!/usr/bin/python3
"""
Fonction
"""
import sys
import MySQLdb
"""
Import sys, Mysqldb
"""


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username>"
              "<mysql password> <name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=username,
                     passwd=password, db=name)
cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC;")

states = cursor.fetchall()
for state in states:
    print(state)

    cursor.close()
    db.close()
