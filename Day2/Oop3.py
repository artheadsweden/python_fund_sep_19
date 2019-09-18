class Employee:
    raise_amnt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __str__(self):
        return f"{self.first} {self.last} earns {self.pay}"

    def give_raise(self):
        self.pay *= self.raise_amnt


class Developer(Employee):
    raise_amnt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __str__(self):
        return super().__str__() + f" and loves {self.prog_lang}"


class Boss(Employee):
    pass


def main():
    emp1 = Employee("Anna", "Jones", 55000)
    emp2 = Employee("John", "Smith", 47000)

    print(emp1)
    print(emp2)
    dev1 = Developer("Sara", "Andersen", 55000, "Python")
    print(dev1)

    Employee.raise_amnt = 1.03
    emp1.give_raise()
    dev1.give_raise()
    print(emp1)
    print(dev1)

    boss1 = Boss("Peter", "Black", 60000)

    if isinstance(boss1, Boss):
        print(boss1.first, "is a boss")
    else:
        print(boss1.first, "is not a boss")

    if isinstance(emp1, Boss):
        print(emp1.first, "is a boss")
    else:
        print(emp1.first, "is not a boss")

    if isinstance(dev1, Employee):
        print(dev1.first, "is an employee")
    else:
        print(dev1.first, "is not an employee")



if __name__ == '__main__':
    main()
