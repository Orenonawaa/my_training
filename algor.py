nums = [5, 6, 3, 8, 1, 4]

# Алгоритм сортировки пузырьковый:

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
                
bubble_sort(nums) 
print(nums)

# Алгоритм сортировки выборкой:

def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
selection_sort(nums)
print(nums)