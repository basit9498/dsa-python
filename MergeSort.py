import math

arrData = [4, 7, 9, 2, 8, 3, 5]

def marge_arr(arr,start,mid,end):
    new_arr=[]
    left_arr=arr[start:mid+1]
    right_arr=arr[mid+1:end+1]

    i=j=0
    k=start

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            # new_arr.append(right_arr[j])
            arr[k]=right_arr[j]
            j=j+1
        else:
            # new_arr.append(left_arr[i])
            arr[k]=left_arr[i]
            i=i+1

        k=k+1

    while i < len(left_arr):
        # new_arr.append(left_arr[i])
        arr[k] = left_arr[i]
        i=i+1
        k=k+1

    while j < len(right_arr):
        # new_arr.append(right_arr[j])
        arr[k] = right_arr[j]
        j=j+1
        k=k+1

    print("left_array",left_arr)
    print("right_array", right_arr)
    print("new", arr)



def marge_sort(arr,start_index,end_index):
    # print("start_index",start_index,"end:",end_index)

    if start_index >= end_index:
        return
    mid = (start_index + end_index) // 2


    marge_sort(arr,start_index,mid)
    marge_sort(arr,mid+1,end_index)
    print("arr:",arr,":start:",start_index,":mid:",mid,":end:",end_index)
    marge_arr(arr,start_index,mid,end_index)



marge_sort(arrData,0,len(arrData)-1)
# for x in range(0,1):
#     print("x",x)