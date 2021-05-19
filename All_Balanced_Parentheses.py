def counter(start):
    progress = []
    for i in range(len(start)):
        for j in range(1, len(start[0]) + 1):
            sls = start[i][:j] + '()' + start[i][j:]
            progress.append(sls)
    return progress
def balanced_parens(n):
    '''
    balanced_parens(0) => [""]
    balanced_parens(1) => ["()"]
    balanced_parens(2) => ["()()","(())"]
    balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
    '''
    if n == 0:
        return [""]

    start = ["()"]
    while True:
        start = counter(start)
        if int(len(start[0]) // 2) == n:
            return list(set(start))

print(balanced_parens(5))