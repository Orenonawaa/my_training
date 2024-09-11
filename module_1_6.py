# Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Выведите на экран словарь my_dict.
my_dict = {'Aegon I' : 1661, 'Visenya' : 1659, 'Rhaenys' : 1663, 'Maegor I' : 1684, 'Aenys I' : 1688}
print('Dict: ', my_dict)
# Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print('Existing value:  ', my_dict['Maegor I'])
my_dict['Jaehaerys I'] = 1707
print(my_dict.get('Madara Uchiha'))
# Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Aerys II (Mad)' : 1886,
                'Aemond' : 1720})
# Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
print('Deleted value: ', my_dict['Rhaenys'])
del my_dict['Rhaenys']
# Выведите на экран словарь my_dict.
print('Modified dictionary:: ', my_dict)
print()
# Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
# Выведите на экран множество my_set (должны отобразиться только уникальные значения).
my_set = {1, 52, 4, 1, 4, 'Sasuke', (2, 8, 5), 9, 1, 1, 9}
print('Set: ', my_set)
# Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add('Madina')
my_set.add('Albina')
my_set.remove('Sasuke')
print('Modified set: ', my_set)
