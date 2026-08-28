from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        counts = Counter(s)
        
        # 1. Check if s can form a palindrome
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        center = odd_chars[0] if odd_chars else ""
        half_counts = {char: count // 2 for char, count in counts.items()}
        
        def make_palindrome(half: list) -> str:
            h_str = "".join(half)
            return h_str + center + h_str[::-1]

        # 2. Try matching target's prefix of length L down to 0
        for L in range(half_len, -1, -1):
            prefix = list(target[:L])
            prefix_counts = Counter(prefix)
            
            # Verify if target[:L] can be formed with available characters
            if any(half_counts.get(char, 0) < count for char, count in prefix_counts.items()):
                continue
            
            rem_counts = {char: half_counts[char] - prefix_counts.get(char, 0) for char in half_counts}
            
            # Case A: Prefix length is exactly half_len (Exact left-half match)
            if L == half_len:
                cand_pal = make_palindrome(prefix)
                if cand_pal > target:
                    return cand_pal
                continue
            
            # Case B: Prefix length is L < half_len
            # We MUST pick a character strictly larger than target[L] at position L
            for char in sorted(rem_counts.keys()):
                if char > target[L] and rem_counts[char] > 0:
                    rem_counts[char] -= 1
                    
                    # Fill the rest with the smallest available characters
                    suffix = []
                    for c in sorted(rem_counts.keys()):
                        suffix.extend([c] * rem_counts[c])
                    
                    cand_pal = make_palindrome(prefix + [char] + suffix)
                    if cand_pal > target:
                        return cand_pal
                    
                    rem_counts[char] += 1

        return ""