class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name
    


class Mammal(Animal):
    pass

class Predator(Animal):
    pass
    
class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

print("        Список объектов:")
print()
a1 = Predator('Саблезубый тигр')
a2 = Mammal('Корова')
p1 = Flower('Одуванчик')
p2 = Fruit('Грейпфрут')

print(a1.name)
print(p1.name)
print()
print(a1.alive)
print(a2.fed)
print()
a1.eat(p1)
a2.eat(p2)
print()
print(a1.alive)
print(a2.fed)
