from colorama import Fore, Style

def print_result(funcForDecorator):
    def decoratedFunc(*args):
        result = funcForDecorator(*args)
        print(funcForDecorator.__name__)
        if type(result) == list:
            for i in result:
                print(i)
        elif type(result) == dict:
            for i,j in result.items():
                print(i, "=", j)
        else:
            print(result)
        return result
    return decoratedFunc


@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print(Fore.RED + '!!!!!!!!' + Style.RESET_ALL)
    test_1()
    test_2()
    test_3()
    test_4()