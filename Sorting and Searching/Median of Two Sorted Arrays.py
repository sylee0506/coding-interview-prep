#Find the median of the two sorted arrays
#The overall run time complexity should be O(log (m+n))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        target_index = total // 2
        
        #edge case: when either one of list is empty
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (float)(nums2[target_index]+nums2[target_index-1])/2
            else:
                return nums2[target_index]
        elif len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (float)(nums1[target_index]+nums1[target_index-1])/2
            else:
                return nums1[target_index]
        
        i = 0
        j = 0
        cnt = 0
        flag = 0
        while i < len(nums1) and j < len(nums2):
            if cnt == target_index:
                if nums1[i] <= nums2[j]:
                    target_num = nums1[i]
                else:
                    target_num = nums2[j]
                flag = 1
                break
            else:
                if nums1[i] <= nums2[j]:
                    temp_num = nums1[i]
                    i += 1
                elif nums1[i] > nums2[j]:
                    temp_num = nums2[j]
                    j += 1
                cnt += 1
        
        if flag == 1:
            if total % 2 == 0:
                return (float)(target_num + temp_num) / 2
            else:
                return target_num
        else:
            if i == len(nums1):
                while True:
                    if cnt == target_index and total % 2 == 0:
                        return (float)(nums2[j] + temp_num) / 2
                    elif cnt == target_index and total % 2 != 0:
                        return nums2[j]
                    else:
                        temp_num = nums2[j]
                        j += 1
                        cnt += 1
            elif j == len(nums2):
                while True:
                    if cnt == target_index and total % 2 == 0:
                        return (float)(nums1[i] + temp_num) / 2
                    elif cnt == target_index and total % 2 != 0:
                        return nums1[i]
                    else:
                        temp_num = nums1[i]
                        i += 1
                        cnt += 1
        #python good code) by doing this, able to remove duplicate code segments
                '''
                m, n = len(A), len(B)
                if m > n:
                    A, B, m, n = B, A, n, m
                '''


#other solution)
#idea : "if we cut the sorted array to two halves of EQUAL LENGTHS, then median is the AVERAGE OF Max(lower_half) and Min(upper_half)
#python good code)
'''
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
'''
