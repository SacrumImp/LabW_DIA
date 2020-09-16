from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from colorama import Fore

def main():
    rectangle = Rectangle(1, 1, "синий")
    print(Fore.BLUE + str(rectangle))
    circle = Circle(1, "зелёный")
    print(Fore.GREEN + str(circle))
    square = Square(1, "красный")
    print(Fore.RED + str(square))

if __name__ == "__main__":
    main()