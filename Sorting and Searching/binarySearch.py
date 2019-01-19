#O(logn) average & worst

def binarySearch(arr, target):
    left = 0; right = len(arr)-1
    
    while left <= right: #등호 필요!
        mid = (left+right) // 2

        if target > arr[mid]:
            left = mid+1
        elif target < arr[mid]:
            right = mid-1
        elif target == arr[mid]:
            return mid

    return False

arr = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(arr, 3))
print(binarySearch(arr, 13))
print(binarySearch(arr, 32))
print(binarySearch(arr, 99))
