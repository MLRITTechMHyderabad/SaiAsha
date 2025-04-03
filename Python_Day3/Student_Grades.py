students = [("Alice", [85,90,78,92]), ("Bob",[60,65,70,75]),("Charlie",[40,45,50,55]),("David",[90,74,82,67])]
dict = {}
for i in students:
    names = i[0]
    grades = i[1]
    dict[names] = grades
print(dict)

d2 = {}
passcount = 0
for i, j in dict.items():
    sum1 = sum(j)
    avg = sum1/len(j)
    print("Average of "+i+" is: ", avg)
    d2[i] = avg
    if avg >= 50:
        passcount += 1
print(max(d2)," Got highest avearage")
print("Number of students who have passed are: ",passcount)


