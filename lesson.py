class Employee:
    def __init__(self, first, second, last, pay):
        self.first = first
        self.second = second
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.second}"

    def code(self):
        print("I am coding")

    def info(self):
        print("I am coding")


class Dev(Employee):
    def __init__(self, first, second, last, pay, name):
        super().__init__(first, second, last, pay)
        self.name = name

    def info(self):
        super().info()
        print("i am goood coder")


amr1 = Employee("Stepan", "stepanov", "python", 201)
amr2 = Dev("Stepan", "we", "wewewew", "wewew", " wewewe")
print(amr2.info())
print(amr2.info())

print(amr1.last)
print(amr1.fullname())


class Employee:
    """Базовый класс сотрудника"""

    def set_salary(self):
        """Метод для начисления зарплаты"""
        print("Pay salary")


class Developer(Employee):
    """Класс для разработчика"""

    pass


class Client:
    """Класс клиента"""

    def get_payment(self):
        """Метод получения оплаты от клиента"""
        print("Get payment")


system_users = [Employee(), Developer(), Developer(), Client()]

for user in system_users:
    if issubclass(user.__class__, Employee):
        # Если класс объекта сотрудник, то начисляем зарплату
        user.set_salary()
    else:
        # В случае, если объект не является сотрудником, то запрашиваем оплату
        user.get_payment()
