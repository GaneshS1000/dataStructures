#program to perform selection sort

def selectionSort(array,size):
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if array[j]<array[min_index]:
                min_index = j
        array[i],array[min_index]=array[min_index],array[i]

numbers = [34,12,66,33,21,90,76,44,100,200]
size = len(numbers)
selectionSort(numbers,size)
print(numbers)
