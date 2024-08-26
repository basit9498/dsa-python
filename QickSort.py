arrData = [4, 7, 9, 2, 8, 3, 5]


def partition (arr,pivotIndex,lowIndex,hightIndex):
    print("start par-->arr:",arr,"pivotIndex",pivotIndex,"lowIndex",lowIndex,"hightIndex",hightIndex)
    partitionIndex=None

    while(lowIndex<hightIndex):
        while(arr[pivotIndex] >= arr[lowIndex] and lowIndex<hightIndex ):
            lowIndex=lowIndex+1
            print("lowIndex:",lowIndex,"hightIndex",hightIndex)
        while(arr[pivotIndex]< arr[hightIndex]):
            hightIndex=hightIndex-1



        if lowIndex>=hightIndex:
            tempValue = arr[pivotIndex]
            partitionIndex=hightIndex
            arr[pivotIndex] = arr[hightIndex]
            arr[hightIndex] = tempValue


        if lowIndex<hightIndex :
            tempValue = arr[lowIndex]
            arr[lowIndex] = arr[hightIndex]
            arr[hightIndex] = tempValue

    print("test--> update:partitionIndex:",partitionIndex,":lowIndex:",lowIndex,":hightIndex:",hightIndex,"update array",arr)

    return partitionIndex


def qickSort(arr,low,high):
    pivotIndex=low
    lowIndex=low
    hightIndex=high
    if(lowIndex<hightIndex):
        print("send to partition:","pivotIndex",pivotIndex,"lowIndex",lowIndex,"hightIndex",hightIndex)
        partitionIndex =  partition(arr,pivotIndex,lowIndex,hightIndex)
        print("partitionIndex",partitionIndex)
        print("new Array", arr)
        qickSort(arr,lowIndex,partitionIndex-1)
        qickSort(arr,partitionIndex+1,hightIndex)
    else:
        print("no more partitions")






qickSort(arrData,0,len(arrData)-1)