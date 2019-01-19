#divide & conquer
#O(n*log(n)) average and worst case

def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    mid = len(arr)//2 #연산자 // ; int 필요
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left)
    mergeSort(right)

    i=0
    j=0
    k=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1

    while i < len(left):
        arr[k]=left[i]
        i=i+1
        k=k+1

    while j < len(right):
        arr[k]=right[j]
        j=j+1
        k=k+1


arr = [94,26,53,17,77,0,31,3,25,-1,20]
mergeSort(arr)
print(arr)
