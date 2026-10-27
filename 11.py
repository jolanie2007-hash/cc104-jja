def find(a, x):
    for i, v in enumerate(a):
        if v == x: return i
    return -1
print(find([4, 7, 9,7], 7))