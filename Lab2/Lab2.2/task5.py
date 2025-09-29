def cache(func):
    cache_ = {} # storage for our cash

    def wrapper(*args, **kwargs):

        key = (args, frozenset(kwargs.items())) 
        if key in cache_: #if we already hav this key
            print("From cash:", key)
            return cache_[key]
        result = func(*args, **kwargs)
        cache_[key] = result
        return result

    return wrapper


# Пример использования
@cache
def slow_function(x, y):
    return x ** y

print(slow_function(2, 2))  
print(slow_function(2, 2))