#divide & conquer
#O(n*log(n)) average / O(n^2) worst; when all list are already sorted and choose min/max as a pivot

def quickSort(arr,first,last):
    if first >= last: #base case; when len of partition list is one
        return arr

    split = partition(arr,first,last)

    quickSort(arr,first,split-1)
    quickSort(arr,split+1,last)

def partition(arr,first,last):
    pivot = arr[first]
    left = first + 1
    right = last

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right >= left and arr[right] >= pivot:
            right -= 1

        if left>right:
            break
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp

    return right #became new pivot index

arr = [94,26,53,17,77,0,31,3,25,-1,20]
quickSort(arr,0,len(arr)-1) #pivot = first element
print(arr)
