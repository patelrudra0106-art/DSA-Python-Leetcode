class Solution(object):
    def removeElement(self, nums, val):
        # Counter for keeping track of elements other than val
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            # If the element is not val
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count