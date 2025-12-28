#program to perform linear search

numbers = [34,12,66,33,21,90,76,44,100,200]
targetElement = int(input("Enter the target Element:"))
index = 0
for x in numbers:
    if x==targetElement:
        index = numbers.index(x)
    else:
        index = -1
print("Index of the element:",index)