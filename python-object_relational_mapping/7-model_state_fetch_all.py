#!/usr/bin/python3
"""
create a script that lists all for states using
sqlalchemy.
"""
# import moduless
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    
    engine = creating_engine("mysql+mysqldb://{}:{}@loclhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State):
        print("{:d}:{}".format(instance.id, instance.name))
    
    
