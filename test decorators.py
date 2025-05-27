def PrintDecorator(func):
    def wrapper(*args, **kwargs):
        print('Hello',end=' ')
        func(*args, **kwargs)
        print('Please get lost!')
    return wrapper


def AdminDecorator(func):
    def wrapper(*args, **kwargs):
        if args[0] == True:
            print('Admin access granted to', end=' ')
        else:
            print('Access denied to', end=' ')
        return func(*args, **kwargs)
    return wrapper


def PrintName(name):
    print(name, end=' ')

@PrintDecorator
def PrintName2(name):
    print(name,end=' ')

@AdminDecorator
def PrintName3(is_admin,name):
    print(name,end=' ')

if __name__ == "__main__":
    PrintName('What?')
    PrintName2('John')
    PrintName3(True,'John')

    # # Using the decorator directly
    # decorated_function = PrintDecorator(PrintName3)
    # decorated_function('John')

    # *args and **kwargs example -
    # def example(*args, **kwargs):
    #     print(args)  # Tuple of positional arguments
    #     print(kwargs)  # Dict of keyword arguments
    #
    #
    # example(1, 2, a=3, b=4)
    # Output:
    # (1, 2)
    # {'a': 3, 'b': 4}

