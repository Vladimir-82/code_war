def sortt(arr):
    j = len(arr) - 1
    while j:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i],  arr[i + 1] = arr[i + 1],  arr[i]
            i += 1
        j -= 1
    return arr


mass = [99, 1, -5, -10, -1000, 77]
print(sortt(mass))