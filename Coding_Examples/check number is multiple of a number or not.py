number1 = int(input("Enter Number to Check: "))
number2 = int(input("Check {} is multiple of ? ".format(number1)))

if number1 % number2 == 0:
    print("Yes, {} is Multiple of {}".format(number1,number2))
else:
    print("No, {} is not Multiple of {}".format(number1,number2))