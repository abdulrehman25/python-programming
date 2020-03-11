rows = int(input("Enter Number of Rows: "))

for i in range(0,rows):
    for j in range(i,rows):
        print(" ",end="")
    for k in range(0,(2 * i - 1)):
        print("*",end="")
    print()
    if i == rows//2:
        for i in range(rows//2 - 1,0,-1):
            for j in range(rows, i, -1):
                print(" ", end="")
            for k in range((2 * i - 1), 0, -1):
                print("*", end="")
            print()
        break

# h = int(input("please enter diamond's height:"))
#
# for i in range(h):
#     print(" "*(h-i), "*"*(i*2+1))
# for i in range(h-2, -1, -1):
#     print(" "*(h-i), "*"*(i*2+1))
import pdb; pdb.set_trace()