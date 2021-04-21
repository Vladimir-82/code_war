def sum_pairs(ints, s):
    '''
    Given a list of integers and a single sum value, return the first two values (parse from the left please)
    in order of appearance that add up to form the sum.
    sum_pairs([11, 3, 7, 5],         10)
    #              ^--^      3 + 7 = 10
    == [3, 7]

    sum_pairs([4, 3, 2, 3, 4],         6)
    #          ^-----^         4 + 2 = 6, indices: 0, 2 *
    #             ^-----^      3 + 3 = 6, indices: 1, 3
    #                ^-----^   2 + 4 = 6, indices: 2, 4
    #  * entire pair is earlier, and therefore is the correct answer
    == [4, 2]

    sum_pairs([0, 0, -2, 3], 2)
    #  there are no pairs of values that can be added to produce 2.
    == None/nil/undefined (Based on the language)
    '''

    summ = []
    for i in ints:
        for j in ints:
            res = i + j
            if res == s and i != j:
                summ.append([i, j])
    return None if not summ else summ[0]

    # summ = []
    # for k in range(len(ints) - 1):
    #     for i in range(1 + k, len(ints)):
    #         res = ints[k] + ints[i]
    #         if res == s:
    #             summ.append([ints[k], ints[i]])
print(sum_pairs([11, 3, 7, 5],         10))