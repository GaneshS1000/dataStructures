#program to perform Binary Search

numbers = [11,20,21,22,25,27,29,30,36,40,50,60,78,88,90,98,100,120,150]
targetElement = int(input("Enter the Target Element:"))
index = -1
flag = True
mid = numbers[len(numbers)//2]
if targetElement == mid:
    index = numbers.index(mid)
elif targetElement<mid:
    for i in range(len(numbers[:mid])):
        if numbers[i]==targetElement:
            index = numbers.index(numbers[i])
        else:
             flag = False
elif targetElement>mid:
    for i in range(numbers.index(mid),len(numbers)):
        if numbers[i] == targetElement:
            index = numbers.index(numbers[i])
        else:
            flag = False

print("Element is Found at:", index)
