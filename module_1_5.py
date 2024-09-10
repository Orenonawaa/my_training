# Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = 1, 4, 'школа', False, 4, [5, 2]
# Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var)


# Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
immutable_var[1] = 52
print(immutable_var) # TypeError: 'tuple' object does not support item assignment. Элементы кортежа не могу быть переназначены.


# Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [1, 2, 3, 4, 'Игра', 'Бокс', True]
print(mutable_list)
# Измените элементы списка mutable_list.
mutable_list[4] = 'Учиха Мадара'
mutable_list[5] = False
# Выведите на экран измененный список mutable_list.
print(mutable_list)