arrData = [4, 7, 9, 2, 8, 3, 5]


def insertion_sort(arr):
    for x in range(len(arr)):
        for y in range(x + 1):
            if arr[x] < arr[y]:
                arr[x], arr[y] = arr[y], arr[x]

    print("After sort: ", arr)


print("Before sort:", arrData)
insertion_sort(arrData)
