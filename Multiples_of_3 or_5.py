def solution(number):
    '''
    Если мы перечислим все натуральные числа ниже 10, которые кратны 3 или 5,
    мы получим 3, 5, 6 и 9. Сумма этих кратных 23.

    Завершите решение так, чтобы оно возвращало сумму всех кратных 3 или 5
    числам ниже переданного числа.

    Примечание. Если число кратно 3 и 5, сосчитайте его только один раз.
    Кроме того, если число отрицательное, верните 0 (для языков, в которых они есть)
    '''
    num = [i for i in range(number) if i % 3 == 0 or i % 5 == 0]
    return 0 if number < 0 else sum(num)

print(solution(-1))