n = int(input('Введите число: '))

def factorial(n):

    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    return fact

print(factorial(n))

# Рекурсия
# n = int(input('Введите число: '))

# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)

#  print(factorial_recursive(n))
