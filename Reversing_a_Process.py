import time
def decode(r):
    '''
    Предположим, мы знаем процесс, с помощью которого строка s была преобразована в строку r (см. Объяснение ниже).
    Цель ката - декодировать эту строку r, чтобы вернуть исходную строку s.
    Объяснение процесса кодирования:
    ввод: строка s, состоящая из строчных букв от «a» до «z» и положительное целое число.
    мы знаем, что существует соответствие между abcde ... uvwxyzи 0, 1, 2 ..., 23, 24, 25: 0 <-> a, 1 <-> b ...
    если c является символом s, которому соответствует номер x, примените к x функцию f: x-> f (x) = num * x% 26,
    затем найдите ch соответствующий символ f (x)
    Накопите все эти ch в строку r
    объединить num и r и вернуть результат

    Например:
    encode ("mer", 6015) -> "6015ekx"

    м -> 12, 12 * 60 15% 26 = 4, 4 -> е
    e -> 4, 4 * 60 15% 26 = 10, 10 -> k
    г -> 17, 17 * 60 15% 26 = 23, 23 -> х

    Таким образом, мы получаем «ekx», следовательно, на выходе получаем «6015ekx».
    Задача
    Строка s была закодирована в строку r описанным выше процессом. завершите функцию, чтобы вернуть s,
    когда это возможно.
    В самом деле, может случиться так, что декодирование невозможно для строк, состоящих из любых букв от «a» до «z»,
    если положительное целое число не было правильно выбрано. В этом случае верните «Невозможно декодировать».

    Examples

    decode "6015ekx" -> "mer"
    decode "5057aan" -> "Impossible to decode"

    '''
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    code_num = ''
    for i in r:
        if i not in alfabet:
            code_num += i
    code_num = int(code_num)
    for i in r:
        if i in alfabet:
            decode_index = alfabet.find(i)
            x = 0
            for j in range(26):
                y = (26 * x + decode_index) // code_num
                print(y)
                output += alfabet[y]
                x += 1


    return output
start = time.time()
print(decode("6015ekx"))
finish = time.time()
print(finish - start)

# alfabet = 'abcdefghijklmnopqrstuvwxyz'
# output = ''
# code_num = ''
# for i in r:
#     if i not in alfabet:
#         code_num += i
# code_num = int(code_num)
# for i in r:
#     if i in alfabet:
#         decode_index = alfabet.find(i)
#         x = 1
#         while True:
#             y = (26 * x + decode_index) / code_num
#             if y % 1 == 0:
#                 output += alfabet[int(y)]
#                 print(y)
#                 break
#             else:
#                 x += 1
# return output


