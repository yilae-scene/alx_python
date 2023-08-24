'''
a module that uses the states name
from CLI input to display all cities
'''
# import modules
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], port=3306, db=sys.argv[3])

    cur = mydb.cursor()
    if 'TURNICATE' in sys.argv[4] \
            or 'SELECT' in sys.argv[4] \
            or 'DROP' in sys.argv[4] \
            or 'DELETE' in sys.argv[4]:
        print('using not allowed keywords')

    else:
        cur.execute("SELECT cities.name FROM cities \
                    INNER JOIN states ON \
                    cities.state_id = states.id \
                    WHERE states.name = '{}' \
                    ORDER BY cities.id".format(sys.argv[4]))

        # fetch the results
        results = cur.fetchall()
        # print results
        result1 = [','.join(i) for i in results]
        if len(result1) == 0:
            print(' ')
        for i in range(len(result1)):
            if i != len(result1) - 1:
                print(result1[i], end=', ')
            else:
                print(result1[i])

        # print(', '.join([i if not isinstance(i, tuple)
        #       else ', '.join(i) for i in results]))

        # commit and fetch
        mydb.commit()
        cur.close()
