# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":

# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average1 = sum(grades[0]) / len(grades[0])
average2 = sum(grades[1]) / len(grades[1])
average3 = sum(grades[2]) / len(grades[2])
average4 = sum(grades[3]) / len(grades[3])
average5 = sum(grades[4]) / len(grades[4])

students1 = tuple(students)

slovar = {students1[0] : average1, students1[1] : average2, students1[2] : average3, students1[3] : average4, students1[4] : average5}
print(slovar)