arrData = [4, 7, 9, 2,2, 8, 3, 5]


def bubble_sort(arr):
    for i in range(len(arr)):
        deduct = i + 1
        for x in range(len(arr) - deduct):
            if x < len(arr) - i + 1:
                if arr[x] > arr[x + 1]:
                    temp = arr[x]
                    arr[x] = arr[x + 1]
                    arr[x + 1] = temp

    print("After sort: ", arr)


print("Before sort:", arrData)
bubble_sort(arrData)
