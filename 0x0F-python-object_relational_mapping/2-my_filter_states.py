#!/usr/bin/python3
"""
    Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

def main():
    conn = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost", passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
