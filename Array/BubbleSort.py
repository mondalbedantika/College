def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
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
print(BubbleSort(arr))