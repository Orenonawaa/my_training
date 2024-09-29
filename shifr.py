# 20: 4, 5, 10, 20
# 19: 19
# 18: 3, 6, 9, 18
# 17: 17
# 16: 4, 8, 16
# 15: 3, 5, 15
# 14: 7, 14
# 13: 13
# 12: 3, 4, 6, 12
# 11: 11
# 10: 5, 10
# 9: 3
# 8: 4, 8
# 7: 7
# 6: 3, 6
# 5: 5
# 4: 4
# 3: 3
N = int(input("Введите число из первой таблички: "))
deliteli = []
for i in range(3,(N//2) + 1):
    if N % i == 0:
        deliteli.append(i)
deliteli.append(N)

ans = str()
for j in range(1, N):
    for i in deliteli:
        if j < i // 2 + 1 and i != i - j:
            ans += f"{j}{i-j}"
print(ans)