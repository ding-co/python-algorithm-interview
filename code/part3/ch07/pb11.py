class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # T.C: O(n), S.C: O(1)
        
        result = []
        
        p = 1
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]
            
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= p
            p *= nums[i]
        
        return result


# Reference Solution
# T.C: O(n), S.C: O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # T.C: O(n), S.C: O(n)
        
#         result = []
        
#         left = []
#         p = 1
#         for i in range(len(nums)):
#             left.append(p)
#             p *= nums[i]
        
#         right = []
#         p = 1
#         for i in range(len(nums) - 1, -1, -1):
#             right.append(p)
#             p *= nums[i]
        
#         for i in range(len(nums)):
#             result.append(left[i] * right[len(nums) - 1 - i])
        
#         return result