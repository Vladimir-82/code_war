import time
def sukuna(n):
    '''
    example: if n = 10 then output will be 7, as 4 is representable as 2^2,
    8 as 2^3 and 9 as 3^2. So the numbers left are 1,2,3,5,6,7,10.
    '''
    i, j = 2, 2
    out = set()
    while i ** j <= n:
        while i ** j <= n:
            mult = i ** j
            if mult <= n:
                out.add(mult)
            j += 1
        i += 1
        j = 2
    return n - len(out)

start = time.time()
print(sukuna(1000000))
finish = time.time()
print(finish - start)

# numbers = {i for i in range(1, n + 1)}
#     out = set([])
#     i, j = 2, 2
#     while True:
#         mult = i ** j
#         if mult in numbers:
#             out.add(mult)
#         j += 1
#         if j > int(n**0.5):
#             j = 2
#             i += 1
#             if i > int(n**0.5):
#                 break
#
#     return len(numbers) - len(out)
#
# start = time.time()
# print(sukuna(1000000))
# finish = time.time()
# print(finish - start)
