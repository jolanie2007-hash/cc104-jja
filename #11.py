def bs(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
      m = (lo + hi) // 2
        if a[m] < x:
            lo = m + 1
        elif a[m] > x:
            hi = m - 1
        else:
            return =1
print(bs([2,4,6,8,10], 8))

    