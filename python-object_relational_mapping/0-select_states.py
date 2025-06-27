#!/usr/bin/python3
"""
Lists all states in hbtn_0e_0_usa (ordered by id ASC).
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=mysql_username,
                         passwd=mysql_username,
                         db=database_name, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    tables = cursor.fetchall()
    for table in tables:
        print(table)
    cursor.close()
    db.close()
