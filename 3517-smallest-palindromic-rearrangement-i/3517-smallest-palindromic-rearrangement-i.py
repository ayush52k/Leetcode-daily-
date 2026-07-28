from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        left_half = []
        mid = ""
        
        # Process characters in alphabetical order ('a' to 'z')
        for char in sorted(freq.keys()):
            count = freq[char]
            if count % 2 != 0:
                mid = char
            left_half.append(char * (count // 2))
            
        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]