def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        # Find middle index
        mid = (left + right) // 2

        # If target found
        if arr[mid] == target:
            return mid

        # If target is bigger
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller
        else:
            right = mid - 1

    return -1

n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")

for i in range(n):
    element = int(input())
    arr.append(element)

# Sort the array
arr.sort()

print("Sorted array:", arr)

target = int(input("Enter element to search: "))

# Function call
result = binary_search(arr, target)

# Output
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")