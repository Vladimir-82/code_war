def snail(snail_map):
    if snail_map == [[]]:
        return []
    if snail_map == [[1]]:
        return [1]
    res = []
    i = 0
    j = 0
    round = 0
    while True:
        round += 1
        while True:

            if snail_map[i][j] != None:
                res.append(snail_map[i][j])
                snail_map[i][j] = None
            else:
                break
            j += 1
            if j == len(snail_map) - round:
                break

        if len(res) == len(snail_map) ** 2:
            return res

        while True:
            if snail_map[i][j] != None:
                res.append(snail_map[i][j])

                snail_map[i][j] = None
            else:
                break
            i += 1
            if i == len(snail_map) - round:
                break

        if len(res) == len(snail_map) ** 2:
            return res

        while True:
            if snail_map[i][j] != None:
                res.append(snail_map[i][j])

                snail_map[i][j] = None
            else:
                break
            j -= 1
            if j == round - 1:
                break

        if len(res) == len(snail_map) ** 2:
            return res

        while True:
            if snail_map[i][j] != None:
                res.append(snail_map[i][j])

                snail_map[i][j] = None
            else:
                break
            i -= 1
            if snail_map[i][j] == None:
                j += 1
                i += 1
                break

        if len(res) == len(snail_map) ** 2:
            return res





array = [[1,  2,   3,  4,   5],
         [16, 17, 18,  19,  6],
         [15, 24, 25,  20,  7],
         [14, 23,  22, 21 , 8],
         [13, 12,  11, 10 , 9]
         ]


# array = [[1,   2, 3,  4],
#          [12, 13, 14, 5],
#          [11, 16, 15, 6],
#          [10, 9,  8,  7]
#          ]




# array = [[1, 2, 3],
#          [8, 9, 4],
#          [7, 6, 5]]


# array = [[1, 2], [3, 4]]
print(snail(array))


Traceback (most recent call last):
  File "/workspace/default/src/codewars-test/codewars_test/test_framework.py", line 111, in wrapper
    func()
  File "tests.py", line 66, in it_1
    test.assert_equals(snail(a), solution(b))
  File "/workspace/default/solution.py", line 14, in snail
    if snail_map[i][j] != None:
IndexError: list index out of range