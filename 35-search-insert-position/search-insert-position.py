class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        miss = nums[:]
        while  target in nums:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        miss.append(target)
        miss.sort()
        return miss.index(target)
        

            