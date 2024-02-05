import pprint

# Классы
print(type(int))


class FirstClass:
    pass


f = FirstClass()
print(f)


class Employee:  # класс
    BASE_SALARY = 10000  # поле класса

    def __init__(self, name: str, place: str):  # инициализатор
        self.name = name  # поле экземпляра
        self.place = place

    @classmethod
    def change_base_salary(cls, value: int):  # метод класса
        cls.BASE_SALARY = value
        return cls.BASE_SALARY

    def change_salary(self, value: int):  # метод экземпляра
        self.BASE_SALARY = value
        return self.BASE_SALARY

    def show(self):  # метод экземпляра
        return f'Name: {self.name}. Place: {self.place}'

    @staticmethod
    def now():
        import date_time
        return datetime.datetime.now()

    def __str__(self):  # строковое представление объекта
        return f'Name: {self.name}. Place: {self.place}'

    def __repr__(self):  # представление объекта как в коде
        return f'{self.__class__.__name__}' \
               f'({self.name}, {self.place})'


employee_1 = Employee('John', 'A1')
# Employee.__init__()
employee_2 = Employee('Bob', 'A2')
print(employee_1.name)
print(employee_2.name)
# print(employee_1.surname)  # AttributeError: 'Employee' object has no attribute 'surname'
pprint.pprint(dir(employee_1))
# employee_1.BASE_SALARY = 5000
print(employee_1.BASE_SALARY)  # 5000
print(employee_2.BASE_SALARY)  # 10000
Employee.BASE_SALARY = 40000
print(employee_1.BASE_SALARY)  # 5000
print(employee_2.BASE_SALARY)  # 40000
print(employee_1.__dict__)
print(employee_2.__dict__)
employee_2.surname = 'Silver'
print(employee_2.__dict__)
print('*' * 50)
print(employee_1.BASE_SALARY)
print(employee_2.BASE_SALARY)
employee_1.change_base_salary(1234)
print(employee_1.BASE_SALARY)
print(employee_2.BASE_SALARY)
employee_2.change_base_salary(4321)
print(employee_1.BASE_SALARY)
print(employee_2.BASE_SALARY)
print(Employee.BASE_SALARY)
print(employee_1.show())
print(employee_1)
print(employee_2.__repr__())
my_list = [employee_2, employee_1]
for emp in my_list:
    print(emp.now())
print(Employee.now())
Employee.change_salary(employee_1, 767)


class Employee:  # класс
    def __init__(self, name: str, place: str):  # инициализатор
        self._name = name  # поле экземпляра
        self.__place = place

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value: str):
        if isinstance(value, str):
            self.__place = value
            return
        raise ValueError('Значение должно быть строкой.')

    def __str__(self):  # строковое представление объекта
        return f'Name: {self._name}. Place: {self.__place}'


employee = Employee('John', 'A1')
# employee.place = 'A3'
# print(employee._Employee__place)
print(employee.place)
# employee.place = 1
print(employee.place)
print(employee.__dict__)


# name - public
# _name - protected
# __name - private


class MultiNumber:
    def __init__(self, *args: int):
        self.value = args

    def __str__(self):
        return f'{self.value}'

    def __add__(self, other):  # +
        if not isinstance(other, (int, float)):
            raise ValueError('Данный тип данных не поддерживается!')
        temp = []
        for val in self.value:
            temp.append(val + other)
        return tuple(temp)

    # def __iadd__(self, other):  # +=
    #     pass

    def __radd__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError('Данный тип данных не поддерживается!')
        temp = []
        for val in self.value:
            temp.append(val + other)
        return tuple(temp)

    def __sub__(self, other):  # -
        if not isinstance(other, (int, float)):
            raise ValueError('Данный тип данных не поддерживается!')
        temp = []
        for val in self.value:
            temp.append(val - other)
        return tuple(temp)

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):  # ==
        if isinstance(other, MultiNumber):
            return self.value == other.value
        return False

    def __len__(self):
        return len(self.value)

    def __bool__(self):
        return bool(self.value)


# value = MultiNumber(1, 2, 3)
# print(value)
# result = value + 1
# print(result)
# result = 10 + value
# print(result)
# result = value - 4
# print(result)
# print(hash(value))

# value_1 = MultiNumber(1, 2, 3)
# value_2 = MultiNumber(1, 2, 3)
# my_dict = {
#     value_1: 'hello',
#     value_2: 'world'
# }
# print(my_dict)
# print(my_dict[value_1])
# print(my_dict[value_2])
value_1 = MultiNumber(1, 2, 3)
value_2 = MultiNumber()
print(bool(value_1))
print(bool(value_2))
print(len(value_1))
print(len(value_2))


class DoubleMultiNumber(MultiNumber):
    def __init__(self, *args: int, double_it=True):
        super().__init__(*args)  # вызывает родительские методы
        self.double = double_it

    @property
    def values(self):
        if not self.double:
            return self.value
        temp = []
        for val in self.value:
            temp.append(val * val)
        return tuple(temp)


dv = DoubleMultiNumber(2, 3, 4, 5, double_it=True)
df = DoubleMultiNumber(6, 7, double_it=False)
print(dv.values)
print(df.values)
