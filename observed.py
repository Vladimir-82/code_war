import itertools

def get_pins(observed):
    # feald = [['1',    '2',     '3'],
    #          ['4',    '5',     '6'],
    #          ['7',    '8',     '9'],
    #          [False, '0',     False]
    #          ]
    res = []
    for i in observed:
        if i == '1':
            res.append('124')
        elif i == '2':
            res.append('1235')
        elif i == '3':
            res.append('236')
        elif i == '4':
            res.append('1457')
        elif i == '5':
            res.append('24568')
        elif i == '6':
            res.append('3569')
        elif i == '7':
            res.append('478')
        elif i == '8':
            res.append('57890')
        elif i == '9':
            res.append('689')
        else:
            res.append('80')

    print(res)


get_pins('1234')



# res = []
#     for i in observed:
#         comb = []
#         comb.append(i)
#
#         for j in range(4):
#             if i in feald[j]:
#                 k = feald[j].index(i)
#
#                 if j != 0:
#                     if feald[j - 1][k] != False:
#                         comb.append(feald[j - 1][k])
#                 if j < len(feald) - 1:
#                     if feald[j + 1][k] != False:
#                         comb.append(feald[j + 1][k])
#                 if k != 0:
#                     if feald[j][k - 1] != False:
#                         comb.append(feald[j][k - 1])
#                 if k < len(feald[j]) - 1:
#                     if feald[j][k + 1] != False:
#                         comb.append(feald[j][k + 1])
#                 break
#         res.append(comb)