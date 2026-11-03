def binary_search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

    # Example usage
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 80
result = binary_search(numbers, target)
if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")