'''
we start our projects by importing MySQLdb
and using it to link to MySQL
database we have created before.
'''
# import modules
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], port=3306, db=sys.argv[3])

    # create cursor
    cur = mydb.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE name = {} Order by states.id".format(sys.argv[4]))

    # fetch the results
    results = cur.fetchall()
    for result in results:
        print(result)

    # commit and close
    mydb.commt()
    cur.close()
