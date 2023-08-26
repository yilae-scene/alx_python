"""
create a script that lists all for states using
sqlalchemy.
"""
# import modules
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    path = ("Mysql+Mysqldb://{}:{}@loclhost:3306/{}".format(user, passwd, db))

    mydb = creating_engine(path)
    Session = sessionmaker(bind=mydb)
    session = Session()

    result = session.query(State).all()
    for row in result:
        print ("{}:{} ".format(row.id,row.name))
    