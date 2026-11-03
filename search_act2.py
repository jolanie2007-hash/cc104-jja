data = [2, 6, 10, 18, 22, 26 ]
target = 18

low, high = 0, len(data) - 1
while low <= high:
    mid = (low + high) // 2
    print(low, high, mid, data[mid])  # Expected output: 0 2 5
    if data[mid] == target:
        print("Found", mid)  # Expected output: Found 3
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1