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
        
h1 = House('Башня Эволюция', 18)
h2 = House('ГУМ', 3)
h1.go_to(5)
h2.go_to(10)