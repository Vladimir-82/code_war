def persistence(n):
    '''
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

    For example:
    persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                           # and 4 has only one digit.
    persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                           # 1*2*6 = 12, and finally 1*2 = 2.
    persistence(4) => 0   # Because 4 is already
    '''
    if len(str(n)) == 1:
        return 0
    counter = 0
    while True:
        res = 1
        for i in str(n):
            res *= int(i)

        if len(str(res)) == 1:
            counter += 1
            return counter
        else:
            n = res
            counter += 1
print(persistence(999))