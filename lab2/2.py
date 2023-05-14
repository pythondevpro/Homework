a, b = list(map(int, input('Введите 2 целых числа через пробел: ').split()))

def new_power(a, b):
    return a ** b
print(f"Число {a} в степени {b} = {new_power(a, b)}")
