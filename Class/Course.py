
class Course:
    def __init__(self, name, duration, *books) -> None:
        self.name = name
        self.duration = duration
        self.books = [self.Book(b) for b in books]
    
    def get_duration(self):
        return self.duration
    def get_name(self):
        return self.name
    def __str__(self) -> str:
        return self.name
    def get_books(self):
        return self.books
   
    def show_details(self):
        print("Name:", self.get_name())
        print("Duration", self.get_duration())
        print("Suggested Books: ", end='')
        print(*self.get_books(), sep=', ')
    
    class Book:
        def __init__(self, title) -> None:
            self.title = title

        def __str__(self) -> str:
            return self.title


if __name__ == "__main__":
    c1 = Course("Math", 6, "Math for statistics", "Linear Algebra", "Calculus", "Trigonometry")
    c1.show_details()
