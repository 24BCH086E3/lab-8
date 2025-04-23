import random

nums = {random.randint(15, 45) for _ in range(10)}
print("Original set:", nums)

less_than_30 = len([n for n in nums if n < 30])
print("Count < 30:", less_than_30)

nums = {n for n in nums if n <= 35}
print("Set after removing >35:", nums)
