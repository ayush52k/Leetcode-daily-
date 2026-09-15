class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        i = 0
        
        # Helper function to check if s[l:r+1] is a palindrome
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while i <= n - k:
            # Check for a palindrome of length k starting at i
            if is_palindrome(i, i + k - 1):
                count += 1
                i += k  # Jump past the found palindrome
            # Check for a palindrome of length k + 1 starting at i
            elif i + k < n and is_palindrome(i, i + k):
                count += 1
                i += k + 1  # Jump past the found palindrome
            else:
                i += 1  # Move to the next starting position
                
        return count