#program to perform insertion sort

def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = [34,12,66,33,21,90,76,44,100,200]
insertionSort(numbers)
print(numbers)