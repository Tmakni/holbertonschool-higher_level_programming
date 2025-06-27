#!/usr/bin/python3
"""
Lists all states starting with 'N' from the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()

    query = """
    SELECT id, name
    FROM states
    WHERE name LIKE BINARY 'N%'      -- garder la casse
    ORDER BY id ASC;
    """

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
