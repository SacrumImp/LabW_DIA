from programmingPatterns.webElement import ConcreteWebElementBuilder
from programmingPatterns.director import WebDirector, labelUpdate, buttonClick

if __name__ == "__main__":

    builder = ConcreteWebElementBuilder()
    director = WebDirector(builder)

    director.make_label()
    label = builder.product.printParts()
    assert label == {'text': 'I am <label>', 'visibility': True, 'action': ('updated', labelUpdate)}, "Неправильно создан элемент label"

    director.make_button()
    button = builder.product.printParts()
    assert button == {'height': 30, 'width': 120, 'visibility': True, 'text': 'I am <button>', 'action': ('clicked', buttonClick)}, "Неправильно создан элемент button"

    director.make_link()
    link = builder.product.printParts()
    assert link == {'text': 'I am <a>', 'visibility': True, 'link': 'https://smth.com'}, "Неправильно создан элемент label"

    director.make_radioButton()
    radioButton = builder.product.printParts()
    assert radioButton == {'text': 'I am <radio>', 'connectivity': True, 'mainElement': 'previousElem', 'visibility': True}, "Неправильно создан элемент label"