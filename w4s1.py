# a = int(input(" please enter first number \n"))
# b = int(input("please enter second number \n"))
# type = i
# def add(a, b):
#     result = a + b
#     return result
#
# total = add(a, b)
# print("the total is", total)
from w3s4 import choice

# problem 1
# def greet():
#     message = "Hello from the function"
#
# # version A
# message = "Hello from outside"
#
# def greet():
#     print(message)
#
# greet()
# version B
# def greet():
#     message = "Hello from the function"
#     print(message)
# greet()

# problem 2
# count = 0
#
# def add_one(count):
#     return count + 1
#
# count = add_one(count)
# print("Outside:", count)

# problem 3
# area = 0

# def area_of_rectangle(width, height):
#     area = width * height

# w = float(input("Enter width: \n"))
# h = float(input("Enter height: \n10"))
# area = area_of_rectangle(w, h)
# print(area)

#problem 4 version 1
# amount = int(input("enter amount"))
# rate = 0.2
#
# def calculate_tax(amount):
#  return amount * rate
#
# amount= calculate_tax(amount)
# print(amount)
#problem 4 version 2
# amount = int(input("enter amount"))
# rate = int(input("enter rate"))
# def calculate_tax(amount, rate):
#  return amount * rate
#
# amount= calculate_tax(amount, rate)
# print(amount)

#problem 5
# discount = 0
#
# def apply_discount(price):
#     if price > 100:
#         discount = 10
#         final_price = price - discount
#     else:
#         final_price = price
#     return final_price
#
# p = float(input("Enter price: "))
# result = apply_discount(p)
# print("Final price:", result)

#problem 6
# balance = 0
# def show_menu():
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("0. Exit")
#     choice = input("Enter choice: ")
#     return choice
#
# def deposit(balance):
#     amount = float(input("Amount to deposit: "))
#     if amount > 0:
#         balance = balance + amount
#         print(balance)
#     else:
#         print("invalid amount")
#     return balance
#
# def withdraw(balance):
#     amount = float(input("Amount to withdraw: "))
#     while 0 < amount <= balance:
#         balance = balance - amount
#         print(balance)
#     return balance
#
#
# while True:
#     choice = show_menu()
#     if choice == "1":
#         deposit(balance)
#     elif choice == "2":
#         withdraw(balance)
#     elif choice == "0":
#         break
#     else:
#         print("invalid")
#         break


#activity 7
# total = 0
# def add_mark(mark, total):
#     total = total + mark
#     return total
# mark1 = int(input("Enter mark 1: "))
# total = add_mark(mark1, total)
# mark2 = int(input("Enter mark 2: "))
# total = add_mark(mark2, total)
# print("Total:", total)

#activity 8
# def get_user_details(name, age):
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     return
#
# def print_message(name, age):
#     if age >= 18:
#         print(f"Hello {name}, you are an adult.")
#     else:
#         print(f"Hello {name}, you are under 18.")
#     return

