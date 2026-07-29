import collections

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        MAX_K = 10**6 + 1
        
        # Step 1: Count character frequencies
        count = collections.Counter(s)
        half_count = [0] * 26
        mid_letter = ""
        
        for c, freq in count.items():
            idx = ord(c) - ord('a')
            half_count[idx] = freq // 2
            if freq % 2 == 1:
                mid_letter = c
                
        # Fast nCr capped at MAX_K
        def nCk(n: int, k_val: int) -> int:
            if k_val < 0 or k_val > n:
                return 0
            k_val = min(k_val, n - k_val)
            res = 1
            for i in range(1, k_val + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        # Calculates total distinct multiset permutations capped at MAX_K
        def count_arrangements(cnts: list[int]) -> int:
            total = sum(cnts)
            res = 1
            for freq in cnts:
                if freq > 0:
                    res *= nCk(total, freq)
                    if res >= MAX_K:
                        return MAX_K
                    total -= freq
            return res

        # Step 2: Check if k-th palindrome exists
        if count_arrangements(half_count) < k:
            return ""

        # Step 3: Construct the left half position by position
        half_len = sum(half_count)
        left = []

        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue

                # Try placing character 'a' + i
                half_count[i] -= 1
                arrangements = count_arrangements(half_count)

                if arrangements >= k:
                    # Keep this character
                    left.append(chr(i + ord('a')))
                    break
                else:
                    # Skip all permutations starting with this character
                    k -= arrangements
                    half_count[i] += 1

        # Step 4: Reconstruct full palindrome
        left_str = "".join(left)
        return left_str + mid_letter + left_str[::-1]
    