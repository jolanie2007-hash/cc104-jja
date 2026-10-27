def f(n):
     if n == 0: return
     print(n, end='')
     f(n - 1)
f(3)