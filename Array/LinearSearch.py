def LinearSearch(arr , key):
    n = len(arr)
    for i in range(n):
        if arr[i]==key:
            return print(f"{key} found at index {i}")
        else:
            return print(f"{key} is not found")

from array import array
n = int(input("Enter size of the array : "))
arr = []
for i in range(n):
    val = int(input(f"Enter element {i+1} : "))
    arr.append(val)
key = int(input("Enter the element to be searched : "))
print("Original Array : ")
print(arr)
LinearSearch(arr , key)