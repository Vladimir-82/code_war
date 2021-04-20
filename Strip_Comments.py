def solution(string, markers):
    '''
    Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.


    Given an input string of:

    apples, pears # and bananas
    grapes
    bananas !apples

    The output expected would be:

    apples, pears
    grapes
    bananas
    result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    # result should == "apples, pears\ngrapes\nbananas"
    '''
    splt = string.split('\n')
    print(splt)
    for el in range(len(splt)):
        for symb in splt[el]:
            if symb in markers:
                index = splt[el].find(symb)
                splt[el] = splt[el][:index]
    print(splt)
    splt = [str(i).strip() for i in splt]
    print(splt)
    joy = '\\n'.join(splt)
    return joy


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

# splt = list(string)
#     for el in range(len(splt)):
#         if splt[el] == '\n':
#             splt[el] = '\\n'
#     string = ''.join(splt)
#     output = ''
#     for elem in string:
#         if elem in markers:
#             index = string.find(elem)
#             output += string[:index].strip()
#             string = string[index + 1:]
#             if '\\n' in string:
#                 index_tab = string.find('\\n')
#                 string = string[index_tab:]
#             else:
#                 return output
#
# print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
