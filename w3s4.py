def atm_simple():
 balance = 0.0
 while True:
    print("\n=== Simple ATM ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("0. Exit")
choice = input("Enter choice: ")
if choice == "1":

 while balance > 0:
  balance = balance + input()
  print(balance)
 #  pass
 # elif choice == "2":

 # pass
 # elif choice == "3":

 # pass
 # elif choice == "0":
 # print("Goodbye!")
 # break
 # else:
 # print("Invalid choice, try again.")