class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mergedArr =[]
        i = 0
        j = 0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                mergedArr.append(nums1[i])
                i +=1
            else:
                mergedArr.append(nums2[j])
                j +=1
 
        for k in range(i,m):
            mergedArr.append(nums1[k])
        for k in range(j,n):
            mergedArr.append(nums2[k])
        
        if (m+n) % 2 == 1:
            return mergedArr[(m+n)//2]
        else:
            return (mergedArr[(m+n)//2] + mergedArr[(m+n)//2-1])/2
        


