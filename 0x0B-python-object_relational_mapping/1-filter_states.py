#!/usr/bin/python3
"""Task 1"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
