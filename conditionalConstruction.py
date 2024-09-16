first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second == third:
    print('Найдено 3 совпадения')
elif first == third:
    print('Найдено 2 совпадения')
elif second == third:
    print('Найдено 2 совпадения')
elif first == second:
    print('Найдено 2 совпадения')
else:
    print('Совпадений не найдено (((')