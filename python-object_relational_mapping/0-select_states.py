'''
 we start our projects by importing MySQLdb and using it to link to MySQL database we have created before. 
'''
# import Mysqldb
import MySQLdb

"""
make sure your code works on main page of the python module
"""
if "__name__" == "__main__":
    # create connection to database using mysqldb

    mydb = MySQLdb.connect(host = 'localhost', user = "root", passwd ='MaRcan2011yilikal', port = 3306, db = 'hbtn_0e_0_usa')

    # create cursor
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states")

    # fetch all the selected states
    results = cur.fetchall()
    
    #print all states
    for result in results:
        print(result)
