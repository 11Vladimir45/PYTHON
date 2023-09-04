import pprint

print(type(int))


class FronteClass:
    BASF = 10000

    def __init__(self, name: str, place: str, age: int):
        self.name = name
        self.place = place
        self.age = age
    @classmethod
    def change_basf(cls, value: int):
        cls.BASF = value
        return cls.BASF


front_1 = FronteClass("John", "A1", 37)
front_2 = FronteClass('Bob', 'A2', 48)

print('*'*70)

print(front_1.name)
print(front_2.name)

pprint.pprint(dir(front_1))
front_1.BASF = 7000
print(front_1.__dict__)
print(front_2.__dict__)
print(front_2.__sizeof__())
print(front_1.__sizeof__())
print(front_1.BASF)  # 7000
print(front_2.BASF)  # 10000
FronteClass.BASF = 45000
print(front_1.BASF)  # 70000
print(front_2.BASF)  # 45000

print('*'*70)

print(front_1.BASF)
print(front_2.BASF)
front_1.change_basf(44444)
print(front_1.BASF)
print(front_2.BASF)
front_2.change_basf(55555)
print(front_1.BASF)
print(front_2.BASF)
print(FronteClass.BASF)


def hello(name):
    print('Привет, ' + name)


students = ['Ира', 'Маша', 'Ваня', 'Петя']

for student in students:
    hello(student)