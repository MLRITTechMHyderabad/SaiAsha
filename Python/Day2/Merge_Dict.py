# merging 2 dictionaries

l1 = int(input("Enter length of dictionary-1: "))
d1 = {}
for i in range(l1):
    keys = input("Enter keys: ")
    vals = input("Enter values: ")
    d1[keys] = [vals]

l2 = int(input("Enter length of dictionary-2: "))
d2 = {}
for i in range(l2):
    keys = input("Enter keys: ")
    vals = input("Enter values: ")
    d2[keys] = [vals]

print("Dictionary 1:", d1)
print("Dictionary 2:", d2)

d3 = d1.copy()
for key, val in d2.items():
    if key in d3:
        d3[key].extend(val)
    else:
        d3[key] = val

print("Merged Dictionary:", d3)