def min_permutation(n):
    lst = list(str(n))
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    if '0' not in lst:
        return int(''.join(lst))
    elif n == '0':
        return 0
    else:
        ind_0 = lst.index('0')
        for i in lst[1:]:
            if i != '0':
                ind_not_0 = lst.index(i)
                break
        lst[ind_0], lst[ind_not_0] = lst[ind_not_0], lst[ind_0]
        return int(''.join(lst))
print(min_permutation('0'))