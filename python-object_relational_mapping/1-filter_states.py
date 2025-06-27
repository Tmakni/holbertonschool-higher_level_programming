#!/usr/bin/python3
"""
Lists all states starting with 'N' from hbtn_0e_0_usa (ordered by id ASC).
"""
import sys
import MySQLdb
if __name__ == "__main__":
    user, pwd, db = sys.argv[1:4]

    conn = MySQLdb.connect(
        host="127.0.0.1",    # TCP explicite
        port=3306,
        user=user,
        passwd=pwd,
        db=db,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
