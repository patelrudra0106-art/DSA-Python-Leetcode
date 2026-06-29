class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2) 
        length = len(nums)
        mid = length // 2
        return float(nums[mid] if length % 2 else (nums[mid-1] + nums[mid]) / 2.0)