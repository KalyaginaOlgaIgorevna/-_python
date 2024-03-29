# task4.py
# Считывание строки из стандартного ввода
s = input()

# Преобразование строки в список символов
c = list(s)

# Создание пустого списка m для хранения определенных символов
m = []

# Проверка, является ли введенная строка палиндромом
if s == s[::-1]:
    # Если да, то выводим "Да"
    print("Да")
else:
    # Если нет, перебираем символы в строке
    for i in s:
        # Проверяем, встречается ли символ более одного раза
        if c.count(i) > 1:
            # Находим первое вхождение символа в строку
            n = s.find(i)
            # Определяем длину строки
            lent = len(s)
            # Проверяем, делится ли индекс первого вхождения на 3 без остатка
            if n % 3 == 0:
                # Находим следующее вхождение того же символа
                k = s.find(i, n)
                # Проверяем, делится ли разница индексов вхождений на 4 без остатка
                if (k - n) % 4 == 0:
                    # Если да, добавляем символ в список m
                    m.append(i)
                else:
                    continue
            else:
                continue
        else:
            continue
    # Проверяем, содержит ли список m более одного элемента
    if len(m) > 1:
        # Если да, выводим "ДА"
        print("ДА")
    else:
        # Если нет, выводим "НЕТ"
        print("НЕТ")

