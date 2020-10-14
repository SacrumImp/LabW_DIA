class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = list(items)
        self.uniqItems = set()
        self.index = 0
        try:
            self.ignore_case = bool(kwargs['ignore_case'])
        except (KeyError, TypeError):
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.items):
                raise StopIteration
            else:
                current = self.items[self.index]
                if self.ignore_case == True:
                    current = current.upper()
                if current not in self.uniqItems:
                    self.uniqItems.add(current)
                    return self.items[self.index]
                self.index = self.index + 1

    def __iter__(self):
        return self

if __name__ == "__main__":
    for i in Unique(['а', 'Б', 'в', 'в', 'В'], ignore_case = True):
        print(i)
    print('---')
    for i in Unique(['а', 'Б', 'в', 'в', 'В'], ignore_case = False):
        print(i)
    print('---')
    for i in Unique([1, 1, 1, 1, 2, 2]):
        print(i)