
class Computer:
    def __init__(self, name, make, OS) -> None:
        self.name = name
        self.CPU = self.CPU(make)
        self.OS = self.OS(OS)
    
    
   
    def __str__(self):
        return f'Name: {self.name}\nProcessor: {self.CPU.get_make()}\nOS: {self.OS.get_name()}'
    
    class OS:
        def __init__(self, name) -> None:
            self.name = name

        def get_name(self) -> str:
            return self.name
    
    class CPU:
        def __init__(self, make) -> None:
            self.make = make

        def get_make(self) -> str:
            return self.make


if __name__ == "__main__":
    c1 = Computer("HP EliteBook 1040 14 G9", "12th Gen Intel(R) Core(TM) i5-1245U   1.60 GHz", "Windows 10 Enterprise")
    print(c1)
