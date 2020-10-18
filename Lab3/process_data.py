import json
import sys
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.print_result import print_result
from lab_python_fp.unique import Unique
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random

path = "/Users/vladislavalpeev/Documents/labs/labsPython/Lab3/data_light.json"

with open(path) as f:
    data = json.load(f)

@print_result
def f1(arg):
    return Unique(field(arg, "job-name"), ignore_case = True)

@print_result
def f2(arg):
    return filter(lambda str: str.capitalize().startswith('Программист'), arg)


@print_result
def f3(arg):
    return map(lambda str: "{} с опытом Python".format(str), arg)


@print_result
def f4(arg):
    arg = list(arg)
    listOfSalaries = list(map(lambda str: "зарплата {} руб.".format(str), gen_random(len(list(arg)), 100000, 200000)))
    return list(zip(arg, listOfSalaries))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
