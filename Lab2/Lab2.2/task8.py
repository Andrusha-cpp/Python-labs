import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # time of beginning programm
        res_func = func(*args, **kwargs)
        end_time = time.time()    # time of ending programm
        time_in_ms = (end_time - start_time) * 1000  #translate to milisec
        print(f"Function time: '{func.__name__}': {time_in_ms:.3f} ms") #3f - signs after the point
        return res_func
    return wrapper

# Пример использования
@timing
def example_func(n): #factorial function
    fact = 1
    for num in range(1, n):
        fact *= num
    return fact

example_func(1000)