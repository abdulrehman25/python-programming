hours = int(input("Enter Hours:"))
minutes = int(input("Enter Minutes:"))
seconds = int(input("Enter Seconds:"))

total_seconds = 0

total_seconds += hours*60*60
total_seconds += minutes*60
total_seconds += seconds
print("Total Seconds: ",total_seconds)