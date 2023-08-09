
from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x = 0, y = 0, id = None):
        super().__init(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


