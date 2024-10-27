# Магические здания
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        index = 0
        if len(args) > 0:
            name = args[0]
            cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, etazh):
        self.name = name
        self.etazh = etazh

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)