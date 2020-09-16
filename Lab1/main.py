import sys
import math

print( "\033[34m Алпеев Владислав Сергеевич ИУ5-54Б")

def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

coefficients = {}

# считывание коэффициентов для уравнения
if (len(sys.argv) > 1):
    for i in range(3):
        try:
            coefficients.update({ chr(65+i): float(sys.argv[i+1])})
        except IndexError:
            coefficients.update({ chr(65+i): 0})
        except ValueError:
            coefficients.update({ chr(65+i): 0})
else:
   for i in range(3):
        userArg = input("\033[32m Пожалуйста, введите аргумент {}: ".format(chr(65+i)))
        while not isNumber(userArg):
            userArg = input("\033[31m Пожалуйста, введите аргумент повторно {}: ".format(chr(65+i)))
        coefficients.update({ chr(65+i): float(userArg)})

#решение биквадратного уравнения
roots = []
discriminant = coefficients.get('B') ** 2 - 4 * coefficients.get('A') * coefficients.get('C')

if coefficients.get('A') == 0 and coefficients.get('B') == 0 and coefficients.get('C') == 0:
    print("\033[33m Уравнение имеет бесконечное количество корней!")
elif coefficients.get('A') == 0 and coefficients.get('B') == 0:
    print("\033[33m У уравнения нет корней!")
elif coefficients.get('A') == 0:
    squareRoots = -coefficients.get('C') / coefficients.get('B')
    if squareRoots >= 0:
        roots.append(math.sqrt(squareRoots))
        if squareRoots != 0:
            roots.append(-math.sqrt(squareRoots))
else:
    if discriminant >= 0:
        squareRoots = (-coefficients.get('B') - math.sqrt(discriminant)) / (2 * coefficients.get('A'))
        if squareRoots >= 0:
            roots.append(math.sqrt(squareRoots))
            if squareRoots != 0:
                roots.append(-math.sqrt(squareRoots))
        if discriminant != 0:
            squareRoots = (-coefficients.get('B') + math.sqrt(discriminant)) / (2 * coefficients.get('A'))
            if squareRoots >= 0:
                roots.append(math.sqrt(squareRoots))
                if squareRoots != 0:
                    roots.append(-math.sqrt(squareRoots))