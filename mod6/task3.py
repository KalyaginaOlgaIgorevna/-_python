def get_armstrong_numbers():
    # Начинаем с числа 10, так как числа от 0 до 9 (однозначные) сами по себе считаются числами Армстронга
    num = 10
    while True:
        # Получаем список цифр текущего числа
        digits = [int(x) for x in str(num)]
        # Определяем количество цифр в числе
        power = len(digits)
        # Суммируем цифры числа, возведенные в степень, равную количеству цифр
        sum_of_powers = sum([x ** power for x in digits])
        # Проверяем, является ли текущее число числом Армстронга
        if num == sum_of_powers:
            # Возвращаем найденное число Армстронга
            yield num
        # Переходим к следующему числу
        num += 1

