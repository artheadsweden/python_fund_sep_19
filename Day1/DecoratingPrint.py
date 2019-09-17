from functools import wraps


def redefined_print(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        pre = kwargs.get('start', '')
        if 'start' in kwargs:
            kwargs.pop('start')
        f(pre, *args, **kwargs)
    return wrapper

print = redefined_print(print)


def main():
    print(print.__name__)
    print("Is this working?", "This is string 2", start="!!!")
    print("Hi")

if __name__ == '__main__':
    main()
