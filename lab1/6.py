import random

sum = 0
max = 0
sum_1 = 0
min_2 = 10
max_po_diag = 0

x = [[random.randint(0, 10) for i in range(4)] for j in range(3)]

for i in range(3):
    for j in range(4):
        print(x[i][j], end='\t')
        sum = sum + x[i][j]
        if x[i][j] > max:
            max = x[i][j]
        if i == 0:
            sum_1 = sum_1 + x[i][j]
        if j == 1:
            if x[i][j] < min_2:
                min_2 = x[i][j]
        if i == j:
            if x[i][j] > max_po_diag:
                max_po_diag = x[i][j]
    print()
print()
print('Сумма всех чисел матрицы = ', sum)
print('Максимальный элемент = ', max)
print('Сумма чисел в первой строке = ', sum_1)
print('Минимальный элемент во втором столбце = ', min_2)
print('Максимальный элемент по главной диагонали = ', max_po_diag)
