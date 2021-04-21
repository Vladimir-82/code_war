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
    for el in range(len(splt)):
        for symb in splt[el]:
            if symb in markers:
                index = splt[el].find(symb)
                splt[el] = splt[el][:index]
    splt = [str(i).strip() for i in splt]
    joy = '\\n'.join(splt)
    return joy


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

