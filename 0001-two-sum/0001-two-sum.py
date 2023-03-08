class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_need = {}
        
        for i in range(len(nums)):
            val = target - nums[i]

            if nums[i] in num_need:
                return [num_need[nums[i]], i]
            
            num_need[val] = i
        print(num_need)
                