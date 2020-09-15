import sys

print( "\033[34mАлпеев Владислав Сергеевич ИУ5-54Б")

def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

coefficients = []

# считывание коэффициентов для уравнения
if (len(sys.argv) > 1):
    for i in range(3):
        try:
            coefficients.append(float(sys.argv[i+1]))
        except IndexError:
            coefficients.append(0)
        except ValueError:
            coefficients.append(0)
else:
   for i in range(3):
        userArg = input("\033[32mПожалуйста, введите аргумент {}: ".format(chr(65+i)))
        while not isNumber(userArg):
            userArg = input("\033[31mПожалуйста, введите аргумент повторно {}: ".format(chr(65+i)))
        coefficients.append(float(userArg))



