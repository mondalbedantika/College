def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1 , n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
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
print(SelectionSort(arr))