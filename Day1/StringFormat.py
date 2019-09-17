def main():
    name = "Sara"
    age = 34

    print("Hi there ", name, "! You are ", age, " years old", sep="")
    print("Hi there {0}! You are {1} years old. Bye {0}".format(name, age))
    print(f"Hi there {name}! You are {age} years old.")


if __name__ == '__main__':
    main()
