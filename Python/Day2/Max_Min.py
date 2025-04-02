# Max and min element from a 2D array
rows = int(input("enter array length: "))
cols = int(input("enter sub array length: "))
array = []
for i in range(rows):
    row = []
    for j in range(cols):
        ele = int(input("enter value: "))
        row.append(ele)
    array.append(row) 
print(array)

max_ele = array[0][0]
min_ele = array[0][0]

for i in range(rows):
    for j in range(cols):
        if array[i][j] > max_ele:
            max_ele = array[i][j]
        elif array[i][j] < min_ele:
            min_ele = array[i][j]
print("Max element: ", max_ele)
print("Min element: ", min_ele)