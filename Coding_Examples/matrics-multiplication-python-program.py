rows = int(input("Enter No of Rows:"))
columns = int(input("Enter No of Columns:"))
matrix_1 = []
matrix_2 = []

print("Insert Values In First Matrix:")
for i in range(rows):
    simple_list = []
    for j in range(1,columns+1):
            val = int(input("Value:"))
            simple_list.append(val)
    matrix_1.append(simple_list)
print(matrix_1)
