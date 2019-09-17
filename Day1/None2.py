def default_val(x=10):
    print(x)
    x += 1


def list_adder(name, the_list=None):
    if the_list is None:
        the_list = []
    the_list.append(name)
    return the_list


def main():
    names = list_adder('Peter')
    print(names)
    names = list_adder('Anna')
    print(names)
    names = list_adder('Sue')
    print(names)


if __name__ == '__main__':
    main()
