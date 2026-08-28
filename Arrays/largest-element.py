arr = [10, 5, 8, 20, 3]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element:", largest)
