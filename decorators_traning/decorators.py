def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called")
        result = func(*args, **kwargs)
        print("Somethin is happening after the function is called")
        return result

    return wrapper

@my_decorator
def add_number(*, a: int, b: int) -> int:
    print("Adding numbers...")
    return a - b

result = add_number(a=2, b=6)
print(result)