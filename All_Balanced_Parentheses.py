import itertools
def balanced_parens(n):
    '''
    balanced_parens(0) => [""]
    balanced_parens(1) => ["()"]
    balanced_parens(2) => ["()()","(())"]
    balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
    '''
    start = [""]

    i = 0
    while i < n:
        i = 0
        progress = []
        for j in range(1, len(start) + 1):
            sls = start[i][:j] + '()' + start[i][j:]# j не растет
            progress.append(sls)

        i += 1
        start = progress
    return list(set(progress))


print(balanced_parens(3))
