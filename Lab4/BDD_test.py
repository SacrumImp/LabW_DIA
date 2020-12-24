from abc import ABC
from programmingPatterns.webElement import ConcreateMediator, ConcreteWebElementBuilder
from programmingPatterns.director import WebDirector

if __name__ == "__main__":
    builder = ConcreteWebElementBuilder()
    director = WebDirector(builder)

    director.make_button()
    button = builder.product

    director.make_label()
    label = builder.product

    mediator = ConcreateMediator(button, label)

    button.makeAction()