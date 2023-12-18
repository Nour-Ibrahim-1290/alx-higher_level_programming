#!/usr/bin/python3
"""listing all states from the database using MySQL"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    con = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    
    cursor = con.cursor()  #cursor object is used 4 execution of sql queries
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states on state_id = states.id \
            ORDER BY cities.id ASC;")
    mydata = cursor.fetchall()
    
    for row in mydata:
        print(row)
    
    cursor.close()
    db.close()
