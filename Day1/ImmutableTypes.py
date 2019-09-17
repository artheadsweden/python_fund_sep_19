def main():
    x = 10
    y = 10
    print(id(x))
    print(id(y))
    y += 1
    print(id(x))
    print(id(y))
    y += 1
    print(id(x))
    print(id(y))

    print("-------")
    name1 = "Peter"
    name2 = "Peter"
    print(id(name1))
    print(id(name2))




if __name__ == '__main__':
    main()
