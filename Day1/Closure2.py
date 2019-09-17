def outer(f):
    def inner(g, n):
        return ">>>" + f(g, n) + "<<<"
    return inner


def create_greeting(greeting, name):
    return f"{greeting}, {name}!"

create_greeting = outer(create_greeting)

def main():
    print(create_greeting.__name__)
    msg = create_greeting("Hi", "Anna")
    msg2 = create_greeting("Yo", "Bob")
    print(msg)
    print(msg2)


if __name__ == '__main__':
    main()
