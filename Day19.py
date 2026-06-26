#DP using fib
def fib(n):
  dp = [0]* (n +1)
  dp[0] = 0
  dp[1] = 1

  for i in range(2, n +1)
         dp[i] = dp[i-1] + dp[i -2]
  return dp[n]  


#problem 
n = 10

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b   

# problem 
n = 7

a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print(a)
