def closure():
    msg = 'Hello'

    def display():
        print('x' * 10)
        print(msg)
        print('x' * 10)
    return display

closure()

    