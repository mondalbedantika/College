def BinarySearch(arr , key):
    n = len(arr)
    low = 0 
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1



from array import array
n = int(input("Enter size of the array : "))
arr = []
for i in range(n):
    val = int(input(f"Enter element {i+1} : "))
    arr.append(val)
key = int(input("Enter the element to be searched : "))
print("Original Array : ")
print(arr)
arr.sort()
result = BinarySearch(arr , key)
if(result == -1):
    print(f"{key} is not found")
else:
    print(f"{key} found at index {result}")