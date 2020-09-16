from lab_python_oop.rectangle import Rectangle
from lab_python_oop.figureColor import FigureColor

class Square(Rectangle):

    FIGURE_TYPE = "квадрат"

    @classmethod
    def getFigureType(cls):
        return cls.FIGURE_TYPE

    def __init__(self, side, _color):
        super().__init__(side, side, _color)

    def __repr__(self):
        return "{} {} cо стороной {} и площадью равной {}".format(
            self._color.getColor(), 
            self.getFigureType(), 
            self.width, 
            self.findSquare())