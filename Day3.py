#String Indexing
fruit = "Mango"

print(fruit[0])   
print(fruit[2])    
print(fruit[-1])   
print(fruit[-3])   
#List Indexing
numbers = [100, 200, 300, 400, 500]

print(numbers[0])
print(numbers[3])
print(numbers[-2])

#Function with Default Parameter
class student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print("she's working...")
s1 = student("vinni", 20)
s1.display

  
#Function Using *args
def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(80, 75, 90, 85)






student("Priya", "Python", "Java", "SQL")
