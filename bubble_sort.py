def bubble_sort(arr):

    n = len(arr)

    # Outer loop for number of passes
    for i in range(n):

        # Inner loop for comparisons
        for j in range(0, n - i - 1):

            # Swap if left number is bigger
            if arr[j] > arr[j + 1]:

                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


# User input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Sorting
sorted_numbers = bubble_sort(numbers)

print("Sorted array:", sorted_numbers)