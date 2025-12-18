# score = int(input("Please enter score"))
# if score >= 70:
#     print("Distinction")
# elif score >= 40:
#     print("pass")
# else:
#     print("fail")

#number 2

# score = int(input("Please enter score"))
# if score >= 40:
#     if score >= 70:
#         print("pass with merit")
#     else:
#         print("pass")
# else:
#     print("fail")

#number 3
# age = int(input("please enter age"))
# if age < 5:
#     print("free entry")
# elif 5 >= age <= 17:
#     print("child ticket")
# elif 18 >= age <= 64:
#     print("adult ticket")
# else
#     print("senior ticket")

#number 4
# days_late = int(input("enter days late"))
# if days_late = 0:
#     print("no fine")
# elif 1 >= days_late <= 5:
#     print("fine =£1")
# elif 6 >= days_late <= 10:
#     print("fine = £5")
# else:
#     print(" fine = £10 and membership review")

# #number 5
#
# score = int(input("please enter score"))
# if score >= 40:
#     if score <= 42:
#         print("borderline pass")
#     else:
#         print("clear pass")
# else:
#     print("fail")

#number 6
#
# is_student = str(input("are you student? (yes/no)"))
# if is_student == "yes":
#     age = int(input("enter age"))
#     if age >= 18:
#         print("no discount")
#     else:
#         print("discount applied")
# else:
#     print("no discount")

#number 7

# colour = str(input("enter a colour(red, amber or green)")).lower()
# if colour == "red":
#     print("stop")
# elif colour == "amber":
#     print("get ready")
# elif colour =="green":
#     print("go")
# else:
#     print("invalid colour")

#number 8
# number = int(input("enter number"))
# if (number % 3) == 0 and (number % 5) == 0 and number != 0:
#     print("FizzBuzz")
# elif (number % 3) == 0 and number != 0:
#     print("Fizz")
# elif (number % 5) == 0 and number != 0:
#     print("Buzz")
# else:
#     print("no match")

# number 9
#
# hungry = str(input("are you hungry(yes/no)"))
# if hungry == "no":
#     print("have water and rest")
# elif hungry == "yes":
#     time = str(input("enter time of day(morning, afternoon or evening)"))
#     if time == "morning":
#         print("have breakfast")
#     elif time == "afternoon":
#         print("have lunch")
#     elif time == "evening":
#         print("have dinner")
#     else:
#         print("not a time")
# else:
#     print("have a snack")

#number 10
# course = int(input("enter course mark"))
# exam =int(input("enter course mark"))
# if course <35 or exam < 35:
#     print("automatic fail")
# elif course >= 40 and exam >= 40:
#     print("module passed")
# else:
#     print("module failed")

#number 11

# pin = int(input("enter pin"))
# if pin == 1234:
#     colour = str(input("enter favourite colour")).lower()
#     if colour == "blue":
#         print("access granted")
#     else:
#         print("security answer incorrect")
# else:
#     print("wrong pin")

#number 12
weather = str(input("enter weather")).lower()
mood = str(input("enter mood")).lower()
if weather == "sunny" and mood == "active":
    print("go for a run")
elif weather == "sunny" and mood == "tired":
    print("relax in park")
elif weather == "rainy":
    print("indoor workout")
elif weather == "cold":
    print("gym tyme")
else:
    print("no suggestion available")