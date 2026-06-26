#List Methods (append(), insert(), remove())
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
fruits.insert(1, "Grapes")
fruits.remove("Banana")

print(fruits)

#List Methods (sort(), reverse(), pop())
numbers = [45, 12, 89, 23, 67]

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

numbers.pop()
print("After Pop:", numbers)

#Find the Largest Number in a List
numbers = [15, 42, 8, 91, 27]

largest = max(numbers)

print("Largest Number:", largest)
#Bubble Sort Algorithm
numbers = [5, 2, 8, 1, 9]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted List:", numbers)
