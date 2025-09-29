import datetime #to now time

def log_calls(filename):

    def decorator(func):
        def wrapper(*args, **kwargs):
            
            time = datetime.datetime.now() #what time is now
            line = f"{time} | {func.__name__} | {args} {kwargs}\n"
            
            with open(filename, "a") as file: #use with..as to automaticly close file
                file.write(line)
           
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("file.txt")
def add(a, b):
    return a * b

print(add(2, 3))
print(add(10, 20))