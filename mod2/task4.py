# task4.py
#Если вы введете "42", то программа выведет "101010 52 2A", так как двоичное представление числа 42 - "101010", восьмеричное - "52", а шестнадцатеричное - "2A".  
# Считываем натуральное число
a = int(input())
a_8 = a
a_16 = a
#в 2сс
b = ''
while a > 0:
    b += str(a%2)
    a //= 2
#в 8сс
c = ''
while a_8 > 0:
    c += str(a_8%8)
    a_8 //= 8
#в 16сс
d = ''
while a_16 > 0:
    d += str(a_16%16)
    a_16 //= 16
print(b[::-1], c[::-1], d[::-1])
