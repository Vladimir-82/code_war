def duplicate_count(text):
    spred = []
    lst = list(text.lower())
    counter = 0
    for i in lst:
        if i in spred:
            continue
        if lst.count(i) > 1:
            counter += 1
            if i not in spred:
                spred.append(i)
    return counter


print(duplicate_count("sxYooI2PFmbz7TcaSCvCM0YvUYDECcTvX3EoYZGFDy7rSWNZirKBRNJYiNJ8Ub7eI5ec55vTSN3q1sppWgyA"))