from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    rectangle = Rectangle(1, 1, "синий")
    print(rectangle)
    circle = Circle(1, "зелёный")
    print(circle)
    square = Square(1, "красный")
    print(square)

if __name__ == "__main__":
    main()