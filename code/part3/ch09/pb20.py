class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        PARENTHESIS_PAIR = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for char in s:
            if char not in PARENTHESIS_PAIR:
                stack.append(char)
            elif not stack or stack.pop() != PARENTHESIS_PAIR[char]:
                return False
        
        return len(stack) == 0