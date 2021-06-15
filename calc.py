def parse_molecule(formula):
    for el in formula:
        if el.isdigit():
            index = formula.find(el)
            if formula[index-1].isalpha():
                insert = int(formula[index]) * formula[index-1]
                formula = formula[:index-1] + insert + formula[index+1:]

    return formula


print(parse_molecule('K4[ON(SO3)2]2'))
# return {K: 4, O: 14, N: 2, S: 4}









# def parse_molecule(formula):
#     for el in formula:
#         if el == '(':
#             insert = ''
#             start = formula.find(el)
#             finish = formula.find(')')
#
#             for i in formula[start + 1:finish]:
#                 if i.isdigit():
#
#                 insert += int(formula[finish + 1]) * i
#
#             print(insert)
#             formula = formula[:start] + insert + formula[finish + 1:]
#     return formula
#
#
# print(parse_molecule('K4[ON(SO3)2]2'))
#  return {K: 4, O: 14, N: 2, S: 4}