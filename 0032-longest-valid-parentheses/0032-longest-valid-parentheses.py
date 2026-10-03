class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index for length calculation
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' is unmatched; set it as the new base index
                    stack.append(i)
                else:
                    # Valid substring found: length = current index - last unmatched index
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
    
    