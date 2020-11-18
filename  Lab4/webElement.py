from abc import ABC, abstractmethod, abstractproperty


#Абстрактный класс строителя
class WebElementBuilder(ABC):
    
    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def setName(self):
        pass
    
    @abstractmethod
    def introduce_height(self):
        pass

    @abstractmethod
    def introduce_width(self):
        pass

    @abstractmethod
    def introduce_visibility(self):
        pass

    @abstractmethod
    def introduce_connectivity(self):
        pass

    @abstractmethod
    def introduce_action(self):
        pass

    @abstractmethod
    def introduce_link(self):
        pass

    @abstractmethod
    def introduce_text(self):
        pass


#Конкретный класс строителя
class ConcreteWebElementBuilder(WebElementBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = WebElement()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def setName(self, name):
        self._product.nameOfElement = name
    
    def introduce_height(self, value):
        self._product.add("height", value)

    def introduce_width(self, value):
        self._product.add("width", value)

    def introduce_visibility(self, value):
        self._product.add("visibility", value)
    
    def introduce_connectivity(self, value):
        self._product.add("connectivity", True)
        self._product.add("mainElement", value)
    
    def introduce_action(self, value):
        self._product.add("action", value)

    def introduce_link(self, value):
        self._product.add("link", value)

    def introduce_text(self, value):
        self._product.add("text", value)


#Класс веб элемента
class WebElement():
    def __init__(self):
        self.parts = {}
        self._name = None

    @property
    def nameOfElement(self):
        return self._name

    @nameOfElement.setter
    def nameOfElement(self, nameOfElement):
        self._name = nameOfElement

    def add(self, partName, partValue):
        self.parts.update({partName: partValue})

    def list_parts(self):
        print("\033[33m\n {} \n\033[37m".format(self._name))
        for i, j in self.parts.items():
            print("{} = {}".format(i, j))

#Класс директора
class WebDirector():
    def __init__(self, builder: WebElementBuilder):
        self._builder = builder
    
    def make_label(self):
        self._builder.setName("<label>")
        self._builder.introduce_text("I am <label>")
        self._builder.introduce_visibility(True)
    
    def make_button(self):
        self._builder.setName("<button>")
        self._builder.introduce_height(30)
        self._builder.introduce_width(120)
        self._builder.introduce_visibility(True)
        self._builder.introduce_text("I am <button>")
        self._builder.introduce_action("sampleOfFunc()")
    
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

if __name__ == "__main__":

    builder = ConcreteWebElementBuilder()
    director = WebDirector(builder)

    director.make_label()
    builder.product.list_parts()

    director.make_button()
    builder.product.list_parts()

    director.make_link()
    builder.product.list_parts()

    director.make_radioButton()
    builder.product.list_parts()




    