class Pupils:
    """Школьники"""
    def __init__(self, id, fio, averageMark, idClass):
        self.id = id
        self.fio = fio
        self.averageMark = averageMark
        self.idClass = idClass

class SchoolClass:
    """Классы"""
    def __init__(self, id, number, letter):
        self.id = id
        self.number = number
        self.letter = letter

class Pupils_SchoolClass:
    """Связь многие ко многим между Школьники и Классы"""
    def __init__(self, id, idPupil, idClass):
        self.id = id
        self.idPupil = idPupil
        self.idClass = idClass

listPupils = [
    Pupils(1, "Васильев Владимир Викторович", 5, 1),
    Pupils(2, "Семенов Кирилл Васильевич", 4, 2),
    Pupils(5, "Демидов Максим Леонидович", 3.6, 1),
    Pupils(7, "Лихачев Виктор Владимирович", 4.6, 3),
    Pupils(12, "Львунин Александр Степанович", 4.6, 3),
    Pupils(14, "Алиев Максим Константинович", 4, 1),
    Pupils(15, "Зубенко Михаил Петрович", 3, 4),
    Pupils(17, "Крищенко Семен Артемович", 5, 4)
]

listSchoolClasses = [
    SchoolClass(1, 4, "А"),
    SchoolClass(2, 6, "А"),
    SchoolClass(3, 4, "Б"),
    SchoolClass(4, 6, "Б")
]

listPupils_SchoolClass = [
    Pupils_SchoolClass(1, 1, 1),
    Pupils_SchoolClass(2, 2, 2),
    Pupils_SchoolClass(3, 5, 1),
    Pupils_SchoolClass(4, 7, 3),
    Pupils_SchoolClass(5, 12, 3),
    Pupils_SchoolClass(6, 14, 1),
    Pupils_SchoolClass(7, 15, 4),
    Pupils_SchoolClass(8, 17, 4),

    Pupils_SchoolClass(9, 1, 3),
    Pupils_SchoolClass(10, 2, 4),
    Pupils_SchoolClass(11, 14, 3),
    Pupils_SchoolClass(12, 17, 2)
]

def main():

    one_to_many = [(i.fio, i.averageMark, j.number, j.letter)
        for i in listPupils
        for j in listSchoolClasses
        if i.idClass == j.id
    ]
    
    many_to_many_temp = [(i.number, i.letter, j.idPupil)
        for i in listSchoolClasses
        for j in listPupils_SchoolClass
        if i.id == j.idClass
    ]

    many_to_many = [(number, letter, j.fio)
        for number, letter, idPupil in many_to_many_temp
        for j in listPupils
        if j.id == idPupil
    ]

    print('Задание Г1')
    res = list(filter(lambda i: i[3].startswith("А"), one_to_many))
    print(res)

    print('\nЗадание Г2')
    res = []
    for i in listSchoolClasses:
        filtered = filter(lambda j: (j[2] == i.number) & (j[3] == i.letter), one_to_many)
        elem = list(sorted(filtered, key=lambda item: item[1], reverse=True))[0]
        res.append((elem[2], elem[3], elem[1]))
    res = sorted(res, key=lambda item: (item[0], item[1]))
    print(res)

    print('\nЗадание Г3')
    res = sorted(many_to_many, key=lambda item: (item[0], item[1]))
    print(res)

if __name__ == '__main__':
    main()
