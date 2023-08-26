"""
create a script that lists all for states using
sqlalchemy.
"""
# import moduless
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

# variables
user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]
if __name__ == "__main__":

    mydb = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db))
    Session = sessionmaker(bind=mydb)
    new_session = Session()

    # print
    results = new_session.query(State).filter(State.name.ilike('%a%')).all()
    
    for result in results:
        print("{}{}".format(result.id, result.name))
