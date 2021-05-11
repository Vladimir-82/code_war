def min_permutation(n):

    res = ''.join(sorted(str(n)))
    if '0' not in str(n):
        return int(res)
    else:
        for i in res:
            if i != '0':
                ind = res.find(i)
                print(ind)
                break
        res = res[ind] + res[1:ind] + '0' + res[ind+1:]
        return int(res)
print(min_permutation(35007))