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

    # path = ("Mysql+Mysqldb://{}:{}@loclhost:3306/{}".format(user, passwd, db))

    # mydb = creating_engine(path)
    # Session = sessionmaker(bind=mydb)
    # new_session = Session()

    # for instance in new_session.query(State):
    #     print("{}:{}".format(instance.id, instance.name))
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State):
        print("{:d}: {}".format(instance.id, instance.name))
