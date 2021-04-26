import time
def sukuna(n):
    '''
    example: if n = 10 then output will be 7, as 4 is representable as 2^2,
    8 as 2^3 and 9 as 3^2. So the numbers left are 1,2,3,5,6,7,10.
    '''

    numbers = [i for i in range(1, n + 1)]
    out = []
    i, j = 2, 2
    while True:
        mult = i ** j
        if mult in numbers:
            out.append(mult)
        j += 1
        if j > int(n**0.5):
            j = 2
            i += 1
            if i > int(n**0.5):
                break

    return len(set(numbers) - set(out))

start = time.time()
print(sukuna(20000))
finish = time.time()
print(finish - start)



# numbers = [i for i in range(1, n + 1)]
#     out = []
#     i, j = 2, 2
#     while True:
#         mult = i ** j
#         if mult in numbers and mult not in out:
#             out.append(mult)
#         j += 1
#         if j > int(n**0.5):
#             j = 2
#             i += 1
#             if i > int(n**0.5):
#                 break
#
#     return n - len(out)
#
# start = time.time()
# print(sukuna(1000000))
# finish = time.time()
# print(finish - start)
