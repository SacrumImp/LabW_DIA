from programmingPatterns.webElement import WebElementBuilder, ConcreteWebElementBuilder

#Класс директора
class WebDirector():
    def __init__(self, builder: WebElementBuilder):
        self._builder = builder
    
    def make_label(self):
        self._builder.setName("<label>")
        self._builder.introduce_text("I am <label>")
        self._builder.introduce_visibility(True)
        self._builder.introduce_action("updated", labelUpdate)
    
    def make_button(self):
        self._builder.setName("<button>")
        self._builder.introduce_height(30)
        self._builder.introduce_width(120)
        self._builder.introduce_visibility(True)
        self._builder.introduce_text("I am <button>")
        self._builder.introduce_action("clicked", buttonClick)
    
    def make_link(self):
        self._builder.setName("<a>")
        self._builder.introduce_text("I am <a>")
        self._builder.introduce_visibility(True)
        self._builder.introduce_link("https://smth.com")

    def make_radioButton(self):
        self._builder.setName("<radio>")
        self._builder.introduce_text("I am <radio>")
        self._builder.introduce_connectivity("previousElem")
        self._builder.introduce_visibility(True)

def labelUpdate():
    print("\n\033[33mДополнительная логика для лейбла\033[33m\n")

def buttonClick():
    print("\n\033[33mДополнительная логика кнопки\033[33m\n")