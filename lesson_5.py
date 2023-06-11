''' Задача #1. Простые числа. '''
'''
def prime_num(num):
    start = 2
    while num % start != 0:
        start += 1
    return start == num

num = int(input('Введите число: '))

print('yes') if prime_num(num) == True else print('no')
'''


''' Задача #2. Вывод элементов. '''
'''
text = ''

def show_nums(num):
    if num == 0:
        return text
    else:
        str_num = input('Введите число: ')
        return text + str_num + show_nums(num-1)

num = int(input('Укажите кол-во элементов: '))

print(show_nums(num)[-1::-1])
'''
