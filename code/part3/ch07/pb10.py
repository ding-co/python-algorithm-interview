class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        pair = []
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                result += min(pair)
                pair = []
        
        return result

# Other Solution 1.
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         nums.sort()
        
#         for idx, n in enumerate(nums):
#             if idx % 2 == 0:
#                 sum += n
        
#         return sum

# Other Solution 2.
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         return sum(sorted(nums)[::2])