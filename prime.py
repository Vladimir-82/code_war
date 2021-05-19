def gen(n):
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
           yield i

def prime(n):
    res = list(gen(n))


    return res
print(prime(23))


# def prime(n):
#     res = []
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             res.append(i)
#     return res, len(res)
# print(prime(23))