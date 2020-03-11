number = int(input("Enter Positive no to Print Table:"))
table_range = int(input("Upto which no?:"))

for i in range(1,table_range+1):
    print(" {} x {} = {}".format(i,number,i*number))