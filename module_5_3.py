# Магические здания
class House:
    def __init__(self, name, etazh):
        self.name = name
        self.etazh = etazh
        
    def go_to(self, new_etazh):
        if new_etazh > self.etazh:
            print("Такого этажа не существует")
            return
        for i in range(1, new_etazh + 1):
            print(i)
            
    def __len__(self):
        return self.etazh
        
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.etazh}'
        isinstance(other, int)
    def __eq__(self, other):
        return self.name == other.name and self.etazh == other.etazh

    def __add__(self, value):
        self.etazh = self.etazh + value
        return self
        
    def __iadd__(self, value):
        self.etazh = self.etazh + value
        return self
    
    def __radd__(self, value):
        self.etazh += value
        return self
    
    def __gt__(self, other):
        return self.etazh > other.etazh
    def __ge__(self, other):
        return self.etazh >= other.etazh
    def __lt__(self, other):
        return self.etazh < other.etazh
    def __le__(self, other):
        return self.etazh <= other.etazh
    def __ne__(self, other):
        return self.etazh != other.etazh
        #
        #
        #
        #
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

