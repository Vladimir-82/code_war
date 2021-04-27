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
    control = len(ints) - 1
    k = 0
    i = 1
    summ = []
    while True:
        res = ints[k] + ints[i]
        if res == s and i <= control:
            summ = [ints[k], ints[i]]
            ints = ints[:i]
            if len(ints) <= 2:
                return summ
            control = i

        i += 1
        if i >= len(ints):
            k += 1
            if k == len(ints) - 1:
                break
            i = k + 1

    return None if not summ else summ
print(sum_pairs([1, 1], 2))


# indx = len(ints) - 1
#     summ = []
#     for k in range(len(ints) - 1):
#         for i in range(1 + k, len(ints)):
#             res = ints[k] + ints[i]
#             if res == s and i <= indx:
#                 summ = [ints[k], ints[i]]
#                 indx = i
#
#     return None if not summ else summ
#


# control = len(ints) - 1
#     k = 0
#     i = 1
#     summ = []
#     while True:
#         res = ints[k] + ints[i]
#         if res == s and i <= control:
#             summ = [ints[k], ints[i]]
#             control = i
#         i += 1
#         if i >= len(ints):
#             k += 1
#             if k == len(ints) - 1:
#                 break
#             i = k + 1
#
#     return None if not summ else summ