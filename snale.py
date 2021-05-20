def snail(snail_map):
    res = []
    i = 0
    j = 0

    while len(res) < len(snail_map) ** 2:
        while j < len(snail_map):
            res.append(snail_map[i][j])
            snail_map[i][j] = None
            j += 1
        i += 1
        j = len(snail_map) - 1
        while i < len(snail_map):
            res.append(snail_map[i][j])
            snail_map[i][j] = None
            i += 1
        i = len(snail_map) - 1
        j -= 1
        while j:
            res.append(snail_map[i][j])
            snail_map[i][j] = None
            j -= 1

        while i:
            res.append(snail_map[i][j])
            snail_map[i][j] = None
            i -= 1

    print(res)











array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(snail(array))