def insert_element(arr , pos , value):
    n = len(arr)
    arr.append(0)
    for i in range(n , pos, -1):
        arr[i] = arr[i-1]
    arr[pos] = value
    return arr


from array import array
n = int(input("Enter size of the array : "))
arr = []
for i in range (n):
    val = int(input(f"Enter element {i+1} : "))
    arr.append(val)
print("Original Array : ")
print(arr)

print(insert_element(arr , 2 , 25))