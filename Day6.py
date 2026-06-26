#Linear Search
numbers = [10, 20, 30, 40, 50]
key = 30

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Found at index", i)
        break
else:
    print("Not Found")
#Binary Search
numbers = [10, 20, 30, 40, 50]
key = 40

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == key:
        print("Found at index", mid)
        break
    elif key > numbers[mid]:
        left = mid + 1
    else:
        right = mid - 1
