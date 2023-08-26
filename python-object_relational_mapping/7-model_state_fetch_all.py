"""
create a script that lists all for states using
sqlalchemy.
"""
# import modules
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]
if __name__ == "__main__":

    path = ("Mysql+Mysqldb://{}:{}@loclhost:3306/{}".format(user, passwd, db))

    mydb = creating_engine(path)
    session = sessionmaker(bind=mydb)
    new_session = session()

    for instance in session.query(State).order_by(State.id):
        print("{}:{}".format(state.id, state.name))
