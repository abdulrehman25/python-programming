rows = int(input("Enter Number of rows:"))

for i in range(1,rows+1):
    for j in range(1,rows-i + 1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
