seen = {}
for x in [2,3,2]:
    seen[x] = seen.get(x, 0) + 1
print(seen)  # Output: {2: 2, 3: 1}