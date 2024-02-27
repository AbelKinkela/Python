# The goal of this exercise is to create an object and make it iterable and work with len() method
# to do this we 
class Orders:
    def __init__(self) -> None:
        self.cart = []
        self.i = 0
    def add_to_cart(self, item):
        self.cart.append(item)
    def remove_from_cart(self, item):
        self.cart.remove(item)

    def __len__(self):
        return len(self.cart)
    
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.i >= len(self.cart):
            raise StopIteration
        else:
            self.i += 1
            return self.cart[self.i - 1]


    def __str__(self) -> str:
        return f'{self.cart}'

if __name__ == "__main__":  
    o1 = Orders()
    o1.add_to_cart("Rice")
    o1.add_to_cart("Tomato")
    o1.add_to_cart("Salt")
    o1.add_to_cart("Fix")
    # unpack the object since its iterable
    #print("Items:",*o1, sep=", ")

    # use len() to calculate the size
    print("Order size: ", len(o1))
    #remove an item from the Order
    o1.remove_from_cart("Rice")
    # loop the object
    for n in o1:
        print(n)