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

print("Insert Values In 2nd Matrix:")
for i in range(rows):
    simple_list = []
    for j in range(1,columns+1):
            val = int(input("Value:"))
            simple_list.append(val)
    matrix_2.append(simple_list)
print(matrix_2)

sum_of_matrixs = []
for i in range(columns):
    sum = 0
    simple_list = []
    for j in range(rows):
        sum += (matrix_1[i][j] * matrix_1[j][i])
    simple_list.append(sum)
    sum_of_matrixs.append(simple_list)
print("Sum of Both Matrixs",sum_of_matrixs)