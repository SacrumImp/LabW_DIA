def generatorFunctionField(dictionaryList, *fields):
    for currentDictionary in dictionaryList:
        keys = currentDictionary.keys()
        newDictionary = dict(currentDictionary)
        for key in keys:
            if key not in fields:
                newDictionary.pop(key)
            elif newDictionary[key] == None:
                newDictionary.pop(key)
        if newDictionary != {}: 
            if len(fields) == 1:
                yield list(newDictionary.values())[0]
            else:
                yield newDictionary

def field(dictionaryList, *fields):
    if len(fields) > 0:
        generatorField = generatorFunctionField(dictionaryList, *fields)
        return list(generatorField)


if __name__ == "__main__":
    dictionaryList = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black', 'size': None},
        {'size': None, 'weight': 15}
    ]
    
    print(field(dictionaryList, 'title'))
    print(field(dictionaryList, 'title', 'price'))
    print(field(dictionaryList, 'title', 'size'))