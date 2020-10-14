from random import randint

def gen_randomFunction(num_count, begin, end):
    for number in range(num_count):
        yield randint(begin, end)

def gen_random(num_count, begin, end):
    generatorRandom = gen_randomFunction(num_count, begin, end)
    return list(generatorRandom)

if __name__ == "__main__":
    print(gen_random(5, 1, 3))