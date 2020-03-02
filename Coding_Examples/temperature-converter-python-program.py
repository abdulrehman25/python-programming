print("Select Converter:")
print("1: C to F")
print("2: F to C")
print("0: exit")

choice = int(input("Select Converter:"))
user_temp = float(input("Enter Temp to Convert:"))
if choice == 1:
    print("You Selected C to F Converter")
    converted_temp = 9/5 * user_temp + 32
elif choice == 2:
    print("You Selected F to C Converter")
    converted_temp = (user_temp - 32) * 5/9
print("Converted Temp is: {}",converted_temp)