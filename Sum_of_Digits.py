def digital_root(n):
    while True:
        sum = 0
        for i in str(n):
            sum += int(i)
        if len(str(sum)) > 1:
            n = sum
        else:
            return sum

print(digital_root(16))