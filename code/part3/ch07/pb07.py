class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target - num]]
            nums_map[num] = i

# Other Solution 1.
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map = {}
#         for i, num in enumerate(nums):
#             nums_map[num] = i
        
#         for i, num in enumerate(nums):
#             if target - num in nums_map and i != nums_map[target - num]:
#                 return [i, nums_map[target - num]]

# Other Solution 2.
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums):
#             complement = target - n
            
#             if complement in nums[i+1:]:
#                 return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]
                