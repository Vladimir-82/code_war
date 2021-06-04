def sum_or_product(arr):
    '''
    ([1, 2, 3],  9),
    ([1, 1, 2],  4),
    ([1, 1, 1],  3),
    ([1],  1),
    ([9],  9),
    ([1, 1],  2),
    ([1, 5],  6),
    ([1, 5, 7],  42),
    ([1, 5, 6],  36),
    ([1, 1, 5, 7],  70),
    ([1, 1, 1, 1],  4),
    ([1, 1, 1, 1, 1],  6),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  1458),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  972),
    ([1, 1, 2, 4, 5],  80),
    ([10, 20, 30],  6000)
    '''

    if len(arr) == 1:
        return arr[0]
    while 1 in arr:
        if 1 <= arr[0] <= 2:
            s = arr[0] + arr[1]
            arr[0:2:] = [s]
            arr.append(arr[0])
            del arr[0]

    n = 1
    for i in arr:
        n *= i
    return n




print(sum_or_product([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))

# while True:
#     if len(arr) == 1:
#         return arr[0]
#
#     if arr[0] == 1 or arr[1] == 1:
#         if 1 <= arr[0] <= 2:
#             s = arr[0] + arr[1]
#             arr[0:2:] = [s]
#
#     else:
#         s = arr[0] * arr[1]
#         arr[0:2:] = [s]
#
#     if arr[0] >= 3:
#         arr.append(arr[0])
#         del arr[0]