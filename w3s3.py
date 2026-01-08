# problem 1
# for i in range(1, 6):  # outer loop
#     for j in range(i): # inner loop
#         print("*", end="")
#     print()
# problem 2
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end="")
#     print()
# problem 3
# num = 1
# for i in range(1, 5):
#     for j in range(i):
#         print(num, end="")
#         num += 1
#     print()
# problem 4
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i*j, end=" ")
#     print()
# problem 5
# for i in range(3):
#     for j in range(4):
#         print(f"({i},{j})", end=" ")
#     print()
# problem 6
# size = 5
# for i in range(size):
#     line = ""
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             line += "*"
#         else:
#             line += " "
#     print(line)
#problem 7
# rows = 4
# for i in range(rows):
#     print(" " * (rows - i - 1), end="")
#     print("*" * (2 * i + 1))
# problem 8
# for j in range(1, 6):
#     for i in range(2, 5):
#         print(f"{i} x {j} = {i*j}", end="  ")
#     print()
# problem 9
# rows = 4
# cols = 6
# for i in range(rows):
#     for j in range(cols):
#         if (i + j) % 2 == 0:
#             print("*", end="")
#         else:
#             print(".", end="")
#     print()
# problem 10
# import math
#
# rows = 5
#
# for i in range(rows):
#     for j in range(i + 1):
#         print(math.comb(i, j), end=" ")
#     print()
