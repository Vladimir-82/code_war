def duplicate_count(text):
    lst = list(text.lower())
    counter = 0
    for i in lst:
        if lst.count(i) > 1:
            counter += 1
            for j in lst:
                if i == j:
                    lst.remove(i)
    return counter


print(duplicate_count("hmksJTFc1kcOdbOz0nZ9fmjMNBBYIHvRRLqROg"))