#!/usr/bin/python3
"""
Lists all states whose name matches exactly the 4th argument

"""
import sys
import MySQLdb


if __name__ == "__main__":
    user, pwd, db, state_name = sys.argv[1:5]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=db,
        charset="utf8"
    )

    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC;"\
        .format(state_name)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
