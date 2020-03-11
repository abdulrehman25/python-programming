no = int(input("Enter a Positive No:"))
while no < 0:
    no = int(input("Enter a Positive No:"))
if no % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")