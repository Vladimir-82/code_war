def min_permutation(n):
    lst = list(str(n))
    i = 0
    while i < len(lst) - 1:

        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
        i += 1
    return lst
print(min_permutation(15317))