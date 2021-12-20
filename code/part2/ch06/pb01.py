# leetcode 125. Valid Palindrome

# My Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = (''.join(ch for ch in s if ch.isalnum())).lower()
        str2 = str1[::-1]
        return str1 == str2

# Other Soultion 1.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for ch in s:
#             if ch.isalnum():
#                 strs.append(ch.lower())
        
#         # check palindrome
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
        
#         return True

# Other Solution 2.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs: Deque = collections.deque()
            
#         for ch in s:
#             if ch.isalnum():
#                 strs.append(ch.lower())
        
#         # check palindrome
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
            
#         return True

# Other Solution 3.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
        
#         # regular expression
#         s = re.sub('[^a-z0-9]', '', s)
        
#         return s == s[::-1]