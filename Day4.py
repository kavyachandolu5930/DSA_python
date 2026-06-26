#String Methods 
text = "welcome to python"

print(text.upper())
print(text.title())
print(text.replace("python", "Java"))
print(text.count("o"))
print(text.startswith("welcome"))

#Palindrome Check
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#Anagram Program
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("The words are Anagrams")
else:
    print("The words are Not Anagrams")
#Count Vowels in a String
text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)
#Recursion 
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of Digits:", sum_digits(num))
10. Recursion – Power of a Number
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))
