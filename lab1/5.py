import random

name = input('Введите свое имя: ')

attempt = 3
count = 1

number_x = random.randint(1, 10)
while count <= 3:
    number = int(input(f'Угадайте число от 1 до 10. У вас {attempt} попытки. Введите число:  '))
    if number == number_x:
        print('Вы угадали!')
    elif number < number_x:
        print(
            f'Ошибка. Ваша попытка неверна. Подсказка: задуманное число больше {number}. Попробуйте еще раз! Введите число: ')
    elif number > number_x:
        print(
            f'Ошибка. Ваша попытка неверна. Подсказка: задуманное число меньше {number}. Попробуйте еще раз! Введите число: ')
    elif number < 0 or number > 10:
        print('Введите число от 1 до 10')
    count += 1
    attempt -= 1
print(f'{name}, игра окончена')
