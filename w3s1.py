#problem 1
# word = str(input("gimme a word u sucker: "))
# n = int(input("gimme a number u sucker: "))
# for i in range(1, n + 1):
#     print(f"{i}: {word}")
from functools import total_ordering

#problem 2
# n = int(input("gimme a number u sucker: "))
#
# total = 0
#
# for i in range(1, n + 1):
#     total += i
#
# print("The sum is:", total)

x = int(input("gimme a number u sucker: "))
for i in range(1, 11):
    print(f"{i} x {x} = {i * x}")