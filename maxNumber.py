#program to find the largest element in the array

#linear approach
numbers = [10, 324, 45, 90, 9808]
max =0
for i in range(len(numbers)):
    if max<numbers[i]:
        max = numbers[i]
print(max)