'''
a module that uses the states name
from CLI input to display all cities
'''
# import modules
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = mydb.cursor()
    if 'TURNICATE' in sys.argv[4] \
            or 'SELECT' in sys.argv[4] \
            or 'DROP' in sys.argv[4] \
            or 'DELETE' in sys.argv[4]:
        print('using not allowed keywords')

    else:
        cur.execute("SELECT * FROM cities \
                    WHERE states_id = \
                    (SELECT states.id \
                    FROM states \
                    WHERE name = '{}' ".format(sys.argv[4]))

        # fetch the results
        results = cur.fetchall()
        for result in results:
            print(result)

        # commit and fetch
        mydb.commit()
        cur.close()
