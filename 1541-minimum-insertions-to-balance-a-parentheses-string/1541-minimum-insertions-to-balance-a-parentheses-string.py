class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        right_needed = 0
        
        for char in s:
            if char == '(':
                # If we need an odd number of ')', we must insert one ')'
                # to complete the pair for the previous '(' before starting a new one
                if right_needed % 2 == 1:
                    insertions += 1
                    right_needed -= 1
                right_needed += 2
            else:  # char == ')'
                right_needed -= 1
                # If we encounter a ')' without a matching '(', insert '('
                if right_needed == -1:
                    insertions += 1
                    right_needed = 1
                    
        return insertions + right_needed