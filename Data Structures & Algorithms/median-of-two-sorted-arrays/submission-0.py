class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #brute force 
        combined = nums1 + nums2
        combined.sort()
        median = 0

        if len(combined) % 2 == 0:
            median = (combined[len(combined) // 2] + combined[(len(combined) // 2) - 1]) / 2
        else:
            median = combined[len(combined) // 2]
        
        return median