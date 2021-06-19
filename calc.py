def parse_molecule(formula):
    formula = list(formula)
    print(formula)
    for i in formula:
        if i.islower():
            index = formula.index(i)
            formula[index - 1] = formula[index - 1] + formula[index]
            del formula[index]
    print(formula)

    for el in formula:
        if el.isdigit():
            index = formula.index(el)
            if formula[index-1].isalpha():
                print(formula[index-1])



    print(formula)


    # dc = {i:formula.count(i) for i in formula}
    # return dc


print(parse_molecule('Mg4[ON(SO3)2]2'))





# def parse_molecule(formula):
#     for el in formula:
#         if el.isdigit():
#             index = formula.find(el)
#             if formula[index-1].isalpha():
#                 insert = int(formula[index]) * formula[index-1]
#                 formula = formula[:index-1] + insert + formula[index+1:]
#     insert = ''
#     for el in formula:
#         if el == '(':
#             start = formula.find(el)
#             finish = formula.find(')')
#
#             for i in formula[start + 1:finish]:
#                 insert += int(formula[finish + 1]) * i
#             formula = formula[:start] + insert + formula[finish + 2:]
#
#     insert = ''
#     for el in formula:
#         if el == '[':
#             start = formula.find(el)
#             finish = formula.find(']')
#
#             for i in formula[start + 1:finish]:
#                 insert += int(formula[finish + 1]) * i
#
#             formula = formula[:start] + insert + formula[finish + 2:]
#
#     dc = {i:formula.count(i) for i in formula if i.isupper()}
#     return dc
#
#
# print(parse_molecule("Mg(OH)2"))