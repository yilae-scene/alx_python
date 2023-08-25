"""
here we connect we import modules sqlalchemy to creat class used to create table.
"""
# import modules
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String
base = declarative_base()


class State(base):
    """ a class that is used to create a table using 
    sqlalchemy:-
     with id : INT
     and name : String attribues
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __int__(self, name):
        self.name = name
