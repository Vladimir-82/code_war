import itertools
def balanced_parens(n):
    '''
    balanced_parens(0) => [""]
    balanced_parens(1) => ["()"]
    balanced_parens(2) => ["()()","(())"]
    balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
    '''
    param = ["()"]

    res = [i * n for i in param]

    print(res)


balanced_parens(2)