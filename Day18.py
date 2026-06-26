#greedy
activities = [(1, 3), (2, 5), (4, 6), (6, 7)]
activities.sort(key=lambda x: x[1])

count = 0
end = 0

for start, finish in activities:
    if start >= end:
        print(start, finish)
        end = finish
        count += 1  


# problem
coins = [10, 5, 2, 1]
amount = 28

count = 0

for coin in coins:
    if amount >= coin:
        count += amount // coin
        amount %= coin

print(count)
