class Product:
    def __init__(self, name: str, weight = int, category = str):
        self.name = name
        self.weight = weight
        self.category = category
    
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    
    def get_products(self):
        """Считывает содержимое файла и возвращает строку со всеми продуктами."""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            # for stroka in file:
            #     print(stroka)
           return file.read()


    def add(self, *products):
        existing_products = self.get_products().split()#splitlines()
        existing_names = {line.split(", ")[0] for line in existing_products}

        with open(self.__file_name, "a", encoding="utf-8") as file:
            for product in products:
                if product.name in existing_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + "\n")
                    print(f"Продукт {product.name} добавлен в магазин")

# Пример использования
if __name__ == "__main__":
    # Создание продуктов
    potato = Product("Potato", 50.0, "Vegetables")
    apple = Product("Apple", 10.5, "Fruits")
    tomato = Product("Tomato", 30.0, "Vegetables")

    # Создание магазина
    shop = Shop()

    # Добавление продуктов
    shop.add(potato, apple)
    shop.add(tomato, potato)  # Попытка добавить дублирующийся продукт