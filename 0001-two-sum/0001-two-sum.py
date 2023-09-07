class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remainders = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if nums[i] in remainders:
                return remainders[nums[i]], i
            else:
                remainders[remainder] = i
        