def type_check(*types): #transmit expected type

    def decorator(func):
        def wrapper(*args, **kwargs):
            
            type_length = len(types)
            args_length = len(args)

            for i in range(type_length):
                if i >= args_length:
                    break  
                if type(args[i]) != types[i] :
                    raise TypeError(f"Argument number {i+1} have to be {types[i].__name__}, "f"get {type(args[i]).__name__}")
                   
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b

print(add(4.01, 3))