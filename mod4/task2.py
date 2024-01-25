# task2.py
# Определение функции st, которая принимает один аргумент n
def st(n):
    # Использование переменной ch внутри функции
    a = ch

    # Проверка, является ли n чётным числом
    if n % 2 == 0:
        # Если n чётное, возврат a в степени n, используя свойство (a^2)^(n/2) = a^n
        return (a**2)**(n/2)
    else:
        # Если n нечётное, возврат a умноженного на a в степени n-1
        return a*(a**(n-1))

# Считывание целочисленного значения из стандартного ввода и сохранение его в переменной ch
ch = int(input())

# Считывание ещё одного целочисленного значения из стандартного ввода и сохранение его в переменной s
s = int(input())

# Вывод результата функции st, передавая ей аргумент s
print(st(s))