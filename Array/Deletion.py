def delete_element(arr , pos):
    if pos < 0 or pos >= len(arr):
        return "Invalid Input"
    
    arr.pop(pos)
    return arr

from array import array
n = int(input("Enter size of the array : "))
arr = []
for i in range (n):
    val = int(input(f"Enter element {i+1} : "))
    arr.append(val)
print("Original Array : ")
print(arr)

print(delete_element(arr , 2))