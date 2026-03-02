from collections import OrderedDict

def cache(maxsize=100):
    def decorator(func):
        memory = OrderedDict()
        def wrapper(*args, **kwargs):
            parameters = (args, tuple(sorted(kwargs.items())))
            if parameters in memory:
                memory.move_to_end(parameters)
            else:
                if len(memory) >= maxsize:
                    memory.popitem(last=False)
                result = func(*args, **kwargs)
                memory[parameters] = result
            # print(memory)
            return memory[parameters]
        return wrapper
    return decorator

@cache(2)
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

print(multiply(1,b=2))
print(multiply(1,b=3))
print(multiply(1,b=2))
print(multiply(1,b=4))
print(multiply(1,b=3))