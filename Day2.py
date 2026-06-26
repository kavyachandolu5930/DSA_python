#Conditinal statements(if,elif,else)
is_cold = True/False

if is_cold:
    print("weather is cold,wear sweater while you go out!")
elif:
    print("it's a hot day")
else:
    print("weather is good! enjoy ur day..")

## 2. Nested Conditionals

has_ticket = True
is_vip = False

if has_ticket:
    if is_vip:
        print("Enter through VIP lounge.")
    else:
        print("Enter through main gate.")
else:
    print("You cannot enter.")

## 3. for Loop

for i in range(5):
    print(i)

## 4. while Loop
i = 1
while i <= 5:
  print(i)
  i += 1
## 5. break and continue

for num in range(1, 4):
    if num == 2:
        continue
    if num == 3:
        break
    print(num)

## Mini Project: Star Patterns
