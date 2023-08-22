'''
we start our projects by importing MySQLdb
and using it to link to MySQL 
database we have created before. 
'''
# import Mysqldb
# import sys
import MySQLdb
import sys
"""
make sure your code works on main page of the python module
"""
if __name__ == "__main__":
    # create connection to database using mysqldb

    mydb = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2],
        port=3306, db=sys.argv[3])

    # create cursor
    cur = mydb.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id")

    # fetch all the selected states
    results = cur.fetchall()

    # print all states
    for result in results:
        print(result)
    mydb.commit()
    cur.close()
