print("!!! Leap Year Checking Program !!!")
user_input = int(input("Enter Year to check: "))
if (user_input % 4 == 0) or (user_input % 100 == 0 and user_input % 400 == 0):
    print("This year {} is leap year".format(user_input))
else:
    print("This year {} is not a leap year".format(user_input))