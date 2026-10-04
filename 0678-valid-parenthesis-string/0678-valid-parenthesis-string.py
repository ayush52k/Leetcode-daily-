class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Minimum required open parentheses
        high = 0  # Maximum potential open parentheses
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            elif char == '*':
                low -= 1   # Treat as ')'
                high += 1  # Treat as '('
            
            # More closing brackets than opening brackets/stars can cover
            if high < 0:
                return False
            
            # 'low' cannot be negative because we can't have negative open brackets
            low = max(low, 0)
        
        # If low is 0, we can match all open parentheses
        return low == 0