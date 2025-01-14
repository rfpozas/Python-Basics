def bubble_sort(arr):
    # outer for loop
    for j in range(len(arr)-1, 0, -1):
        # inner for loop
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# sample list to be sorted
sample_list = [23, 14, 23, 24, 12, 14, 1, 2, 5]

print("Unsorted list:")
print(sample_list)

bubble_sort(sample_list)

print("Sorted list:")
print(sample_list)