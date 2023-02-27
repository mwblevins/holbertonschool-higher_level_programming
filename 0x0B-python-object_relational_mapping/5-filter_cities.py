#!/usr/bin/python3
"""Task 5"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                ORDER BY cities.id")
    cit_lst = [city[2] for city in cur.fetchall() if city[4] == sys.argv[4]]
    print(", ".join(cit_lst))