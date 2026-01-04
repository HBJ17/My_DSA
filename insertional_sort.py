def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]      # element to be inserted
        j = i - 1

        # Shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j + 1] = key

    return arr

arr = [8, 3, 5, 2]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
