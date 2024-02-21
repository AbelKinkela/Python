# At least one method is implemented otherwise it will be an interface


from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def show():
        pass

    def display(self):
        print('Parent Display')

class Child(Parent):
    def show(self):
        print("Show from child")

    def display(self):
        print('Child Display')
        super().display()


c = Child()
c.show()
c.display()
print(Child.mro())