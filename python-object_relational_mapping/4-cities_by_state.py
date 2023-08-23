'''
state all cities with state
name and cities name
'''
# import modules
import MySQLdb
import sys

if __name__ == "__main__":

    mydb = MySQLdb.connect(user = sys.argv[1], host = 'localhost', passwd = sys.argv[2] , db = sys.argv[3])

    # create a cursor
    cur = mydb.cursor()
    cur.execute(
        "SELECT states.id, states.name, cities.name FROM states \
        INNER JOIN cities \
        WHERE states.id = cities.state_id \
        ORDER BY cities.id")

    # fetchall
    results = cur.fetchall()
    for result in results:
        print (result)

    # commit and close
    mydb.commit()
    cur.close()
