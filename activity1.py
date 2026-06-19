#Node
class  Node: 
     def __init__(self,data): 
         self.data = data 
         self.next = None 
Node1 = Node(40) 
Node2 = Node(50) 
Node3 = Node(60)  
 
Node1.next = Node2  
Node2.next = Node3 
Node3.next = Node1

head = Node1

print(head.data) 
print(head.next.data)
print(head.next.next.data)

#class
class dog: 
    def _init_(self, name, age ): 
        self.name = name
        self.age= age
    
    def display(self): 
            print(f'{self.name} is {self.age} days old') 
            
    def bark(self): 
        print("bow bow bow") 
    def sleep(self): 
        print("dog is sleeping...")
d1 = dog("vinni" ,5) 
d1.display() 
d1.bark() 
d1.sleep()

#Minstack
class Minstack: 
    def _init_(self): 
        self.stack = [-1] 
        self.min_stack = [-1] 
    def push(self,value: int ) -> None: 
        self.stack.append(value)
        if not self.min_stack or self.stack[-1]<=self.min_stack[-1]:
             self.min_stack.append(value) 
    def pop(self) -> None:   
           
        if self.stack.pop() ==self.min_stack[-1]: 
            self.min_stack.pop()           
    def top(self)  -> int: 
           return self.stack[-1] 
    def getMin(self) -> int:    
            return self.min_stack[-1]
    
#BubbleSort
def BubbleSort(nums): 
    c=0  
    L=len(nums) 
    for j in range(L):
        swapped=False  
        for i in range(L -1-j):  
           c+=1
           if nums[i] < nums[i+1]: 
             nums[i], nums[i+1] = nums[i+1], nums[i]  
           swapped=True 
           print(c,j,i,nums) 
           if not swapped:  
               break  
    return nums
nums = [5, 4, 3, 2, 1] 
print(BubbleSort(nums))
    
