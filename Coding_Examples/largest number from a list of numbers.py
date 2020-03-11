numbers = []
numbers_count = int(input("How many numbers you want to Input?: "))
for i in range(numbers_count):
    numbers.append((int(input("Enter Number to Add: "))))
largest = 0

for number in numbers:
    if number > largest:
        largest = number
print(largest,"is Largest Number")