arrData = [4, 7, 9, 2, 8, 3, 5]

def selection_sort(arr):
    for x in range(len(arr)):
        min_index = x
        for y in range(x + 1, len(arr)):
            if arr[min_index] > arr[y]:
                min_index = y
        arr[x], arr[min_index] = arr[min_index], arr[x]

    print("After sort: ", arr)


print("Before sort:", arrData)
selection_sort(arrData)
