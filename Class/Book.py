class Book:
    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print(f'Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}')

    def get_price(self):
        return self.price
    
    def get_title(self):
        return self.price
    
    def get_author(self):
        return self.price
    

if __name__ == "__main__":
    c1 = Book('Python Crash Course', 'Eric matthews', '200')
    c1.show_details()