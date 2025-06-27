#!/usr/bin/python3
"""
Lists all states in hbtn_0e_0_usa (id ↑).
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user, pwd, db = sys.argv[1:4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, passwd=pwd, db=db,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
