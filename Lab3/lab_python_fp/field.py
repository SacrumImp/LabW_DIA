def generatorFunctionField(dictionaryList, *fields):
    for i in dictionaryList:
        resultDictionary = {}
        for field in fields:
            try:
                resultDictionary[field] = dictionaryList[field]
            except:
                pass
        yield 

def field(dictionaryList, *fields):
    if len(fields) > 0:
        generatorField = generatorFunctionField(dictionaryList, *fields)
        return list(generatorField)


if __name__ == "__main__":
    dictionaryList = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    
    print(field(dictionaryList, 'title'))
    print(field(dictionaryList, 'title', 'price'))