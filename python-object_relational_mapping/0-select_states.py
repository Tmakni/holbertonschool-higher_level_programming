#!/usr/bin/python3
"""
Lists all states in hbtn_0e_0_usa (ordered by id ASC).
"""
import sys
import MySQLdb


def main():
    """Connects to MySQL, runs the SELECT, prints each row."""
    if len(sys.argv) < 4:
        print("Usage: {} user password database".format(sys.argv[0]))
        return

    user, pwd, db = sys.argv[1:4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=db,
        charset="utf8",
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
