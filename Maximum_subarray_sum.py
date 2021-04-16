# def is_minus(arg):
#     return arg < 0
def max_sequence(arr):

    '''
    Задача подмассива максимальной суммы состоит в нахождении максимальной суммы непрерывной подпоследовательности в массиве или списке целых чисел:
    max_sequence ([- 2, 1, -3, 4, -1, 2, 1, -5, 4])
    должно быть 6: [4, -1, 2, 1]
    Легкий случай - это когда список состоит только из положительных чисел, а максимальная сумма - это сумма всего массива.
    Если список состоит только из отрицательных чисел, вместо этого верните 0.
    Считается, что пустой список имеет нулевую наибольшую сумму. Обратите внимание, что пустой список или массив также
    является допустимым подсписком подмассивом.
    '''
    # if not arr:
    #     return 0
    # if len(list(filter(is_minus, arr))) == len(arr):
    #     return 0
    if all(i < 0 for i in arr) or not arr:
        return 0
    step = 1
    summory_list = []
    for i in range(len(arr)):
        for j in range(step, len(arr) + 1):
            res = arr[i:j]
            summory_list.append(sum(res))
        step += 1
        if step == len(arr):
            break
    return max(summory_list)

print(max_sequence([-5, -7, 2]))
