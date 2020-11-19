from abc import ABC, abstractmethod, abstractproperty


#Класс посредника
class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


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
        self._mediator = None

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
    
    def introduce_action(self, name, value):
        self._product.add("action", (name, value))

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

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator

    @nameOfElement.getter
    def nameOfElement(self):
        return self._name

    def add(self, partName, partValue):
        self.parts.update({partName: partValue})

    def printParts(self):
        print("\033[33m\n {} \n\033[37m".format(self._name))
        for i, j in self.parts.items():
            print("{} = {}".format(i, j))

    def makeAction(self):
        self._mediator.notify(self, self.parts["action"][0])
        func = self.parts["action"][1]
        func()


#Конкретная реализация посредника
class ConcreateMediator(Mediator):
    def __init__(self, webElement1: WebElement, webElement2: WebElement):
        self._webElement1 = webElement1
        self._webElement1.mediator = self
        self._webElement2 = webElement2
        self._webElement2.mediator = self
    
    def notify(self, sender: object, event: str):
        if (event == "clicked") and (sender.nameOfElement == "<button>"):
            print("\033[35m\nНажата кнопка, запрошено обновление label\033[37m\n")
            self._webElement2.makeAction()
        elif (event == "updated") and (sender.nameOfElement == "<label>"):
            print("\033[35m\nПосле нажатия кнопки label был обновлен\033[37m\n")


    