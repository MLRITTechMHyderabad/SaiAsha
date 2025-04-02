# frequency of words in a string
string = input("enter string: ")
words = string.split()
dict = {}
for i in words:
    i = i.lower()
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)