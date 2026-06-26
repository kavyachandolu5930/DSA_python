#Find Second Largest Number
numbers = [10, 25, 40, 15, 30]

numbers.sort()

print("Second Largest:", numbers[-2])

#Bubble Sort
numbers = [5, 3, 8, 1]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

#Selection Sort
numbers = [29, 10, 14, 37]

for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(numbers)
