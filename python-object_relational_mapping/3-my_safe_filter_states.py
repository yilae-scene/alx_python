'''
this is a module that tries to avoid a user input SQL injection
by trying to filter keywords that
might be used by user that will harm the SQL databases.
'''
# import modules
import MySQLdb
import sys

if __name__ == "__main__":

    mydb = MySQLdb.connect(host = 'localhost', user = sys.argv[1] , passwd = sys.argv[2] ,port = 3306,  db = sys.argv[3])
    
    cur = mydb.cursor()

    if 'TRUNCATE' in sys.argv[4] or 'DROP' in sys.argv[4] or 'SELECT' in sys.argv[4] or 'UPDATE' in sys.argv[4] or 'DELETE' in sys.argv[4]:
        print("use only one value")
    else:
        cur.execute("SELECT id, name FROM states WHERE name = '{}'".format(sys.argv[4]))

        # print results
        results = cur.fetchall()
        for result in results:
            print(result)
        # commit and close
        mydb.commit()
        cur.close()
