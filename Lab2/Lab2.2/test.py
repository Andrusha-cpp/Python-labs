def decorate(func):

    def wrapper(*args, **kwargs):

        res = func(*args, **kwargs)
        return res
    
    return wrapper

@decorate
def func(name):
    print(f"Your name is {name}")

name = "Andrew"
func(name)