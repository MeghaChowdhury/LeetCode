class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        n = len(nums) - 1
        for i in range(len(nums)):
            if nums[k] != val:
                k += 1
            else:
                nums[k] = nums[n]
                n -= 1
        return k



        