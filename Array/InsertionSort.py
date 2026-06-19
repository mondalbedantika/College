def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
            
from array import array
n = int(input("Enter size of the array : "))
arr = []
for i in range(n):
    val = int(input(f"Enter element {i+1} : "))
    arr.append(val)
print("Original Array : ")
print(arr)
print("Sorted Array : ")
print(InsertionSort(arr))