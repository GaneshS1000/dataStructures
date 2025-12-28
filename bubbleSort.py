#program to perform bubble sort

numbers = [34,12,66,33,21,90,76,44,100,200]
temp = 0
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]:
            temp = numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=temp
print(numbers)