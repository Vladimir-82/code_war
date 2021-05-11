def min_permutation(n):
    res = ''.join(sorted(str(n)))
    print(res)
    out = ''
    if res[0] != 0:
        return int(res)
    else:
        for i in res:
            if i != '0':
                out += str(int(res[:'0']))
                out += i
                break
        out += str(int(res[res.find('0'):res.find(i)]))
        out += '0'
        out += res[res.find(i)+1:]



        return out
print(min_permutation(-20))