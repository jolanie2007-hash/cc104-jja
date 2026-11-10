def bs(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(bs([2,4,6,8,10], 8))  # Output: 2