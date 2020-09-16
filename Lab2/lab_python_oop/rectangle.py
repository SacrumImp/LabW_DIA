from lab_python_oop.geometricalFigure import GeometricalFigure 
from lab_python_oop.figureColor import FigureColor

class Rectangle(GeometricalFigure):
    
    FIGURE_TYPE =  "прямоугольник"

    @classmethod
    def getFigureType(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, _color):
        self.width = width
        self.height = height
        self._color = FigureColor()
        self._color.setColor(_color)

    def findSquare(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} c шириной равной {}, высотой равной {} и площадью равной {}".format(
            self._color.getColor(), 
            self.getFigureType(), 
            self.width, 
            self.height, 
            self.findSquare())