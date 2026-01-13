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
 # TODO: handle deposit (check amount > 0, update balance)
 while balance > 0:
  balance = balance + input()
  print(balance)
 #  pass
 # elif choice == "2":
 # # TODO: handle withdraw (check > 0, <= balance)
 # pass
 # elif choice == "3":
 # # TODO: show balance formatted to 2 decimal places
 # pass
 # elif choice == "0":
 # print("Goodbye!")
 # break
 # else:
 # print("Invalid choice, try again.")