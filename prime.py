def prime(n):#решето эратосфена
    start = [k for k in range(2, n + 1)]

    for i in start:
        for j in start[start.index(i) + 1:]:
            if j % i == 0:
                start.remove(j)
    return start
print(prime(11))


# def prime(n):перебор
#     res = []
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             res.append(i)
#     return res, len(res)
# print(prime(23))