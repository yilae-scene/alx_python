
# import modules
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Integer, Column, String

"""
here we connect we import modules
sqlalchemy to creat class used
to create table.
"""
base = declarative_base()

if __name__ == "__main__":
    """make sure that your class doesn't work \
    if not imported """

    class State(base):
        """ a class that is used to create a table using 
        sqlalchemy
        """
        """ a class that is used to create a table using 
        sqlalchemy
        Attributes:

         id == that will auto_increment
         name == that used for naming.
        """
        
        __table__ = "state"
        # create columns

        id = Column(Integer, unique=True, autoincrement=True,
                    primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)

        def __int__(self, name):
            self.name = name
