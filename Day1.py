Day 1: Python Fundamentals Programs

1. Basic Input & Output

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
print(f"Hello {name}, you are an adult.")
else:
print(f"Hello {name}, you are not an adult yet.")

2. Variables 

x = 10
y = 10
print("Before change:", x, y)

x = "Hello"
print("After change:", x, y)

3. Data Types 

num = 5              # int
price = 3.14         # float
text = "Python"      # string
is_valid = True      # boolean

print(type(num), type(price), type(text), type(is_valid))

4. Type Casting Example

price_str = "15.50"
price_float = float(price_str)
quantity = 2
total = price_float * quantity

print("Total price:", total)

5. Operators 

a = 10
b = 3

print("Addition:", a + b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Power:", a ** b)

6. Logical Operators Example

is_weekend = True
is_raining = False

go_hiking = is_weekend and not is_raining
print("Can go hiking:", go_hiking)
