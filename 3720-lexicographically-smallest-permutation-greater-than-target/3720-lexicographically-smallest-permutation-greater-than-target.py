from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        # Find the maximum prefix length of target that s can match
        matched_len = 0
        curr_counts = Counter()
        for i in range(n):
            curr_counts[target[i]] += 1
            if curr_counts[target[i]] <= s_counts[target[i]]:
                matched_len = i + 1
            else:
                break
                
        # Try split points i from matched_len down to 0
        # At split point i: prefix target[:i] matches, and s[i] > target[i]
        for i in range(min(matched_len, n - 1), -1, -1):
            prefix_cnt = Counter(target[:i])
            rem_counts = s_counts - prefix_cnt
            
            target_char = target[i]
            # Find the smallest character strictly greater than target[i]
            for char_code in range(ord(target_char) + 1, ord('z') + 1):
                char = chr(char_code)
                if rem_counts[char] > 0:
                    # Construct the lexicographically smallest valid permutation
                    res = list(target[:i])
                    res.append(char)
                    rem_counts[char] -= 1
                    
                    # Fill the rest with remaining characters in sorted order
                    for c_code in range(ord('a'), ord('z') + 1):
                        c = chr(c_code)
                        if rem_counts[c] > 0:
                            res.extend([c] * rem_counts[c])
                    
                    return "".join(res)
                    
        return ""