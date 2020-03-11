# taking input from user

number = int(input("Enter Base Number: "))
power = int(input("Enter Power(Exponent): "))
result = 1

# solving using C method
for i in range(1,power+1):
    result *= number
print("C Method Result is ",result)
# Solving using python method
print("Python Method Result is ",number**power)