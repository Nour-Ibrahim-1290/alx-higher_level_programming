#!/usr/bin/python3
"""listing all states from the database using MySQL"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    try:
        con = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3])
    except MySQLdb.Error:
        print("connection error!")
    
    cursor = con.cursor()  #cursor object is used 4 execution of sql queries
    
    try:
        cursor.execute("SELECT * FROM states ORDER BY states.id")
        data = cursor.fetchall()
    
        for row in data:
            print(row)
    except MySQL.Error:
        print("failed execution!")
    
    cursor.close()
    con.close()
