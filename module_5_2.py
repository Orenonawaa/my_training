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
        
        
h1 = House('Башня Эволюция', 54)
h2 = House('ГУМ', 3)

# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))