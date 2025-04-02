# Matrix transpose
rows = int(input("enter no of rows: "))
cols = int(input("enter no of cols: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        ele = int(input("enter value: "))
        row.append(ele)
    matrix.append(row) 
print(matrix)

transpose = []
for i in range(cols):
    t_rows = []
    for j in range(rows):
        t_rows.append(matrix[j][i])
    transpose.append(t_rows)
print(transpose)