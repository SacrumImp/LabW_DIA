from lab_python_oop.geometricalFigure import GeometricalFigure
from lab_python_oop.figureColor import FigureColor
from math import pi

class Circle(GeometricalFigure):

    FIGURE_TYPE = "круг"

    @classmethod
    def getFigureType(cls):
        return cls.FIGURE_TYPE
    
    def __init__(self, radius, _color):
        self.radius = radius
        self._color = FigureColor()
        self._color.setColor(_color)

    def findSquare(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        return "{} {} c радиусом {} и площадью равной {}".format(
            self._color.getColor(), 
            self.getFigureType(), 
            self.radius, 
            self.findSquare())
