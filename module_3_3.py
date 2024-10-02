print("1. Функция с параметрами по умолчанию:")

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.

print_params()
print_params(1,2,3,4,5,6,7,8,9,0) # тут ошибка вылезает
print_params(52) # тут изменяется переменная "a", а остальные по умолчанию остаются

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

print_params('Alblak', 25, [1, 2, 3])

print("2. Распаковка параметров:")

value_list = ["Йагами Лайт", 52, {'Пароль', 69}]
value_dict = {'a': 52, 'b': 'Дота 2', 'c': True}
print_params(*value_list)
print_params(**value_dict)

print("3.Распаковка + отдельные параметры:")

value_list_2 = ["Call of Duty: Modern Warfare 3", 2011]
print_params(*value_list_2, 42) # Все работает!!!