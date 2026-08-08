from bisect import bisect_left
from collections import defaultdict

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # Store all occurrence indices for each character in word1
        pos = defaultdict(list)
        for idx, ch in enumerate(word1):
            pos[ch].append(idx)
            
        # Helper to find largest index in pos[ch] strictly less than `limit`
        def get_last_less_than(ch, limit):
            if limit <= 0 or ch not in pos:
                return -1
            lst = pos[ch]
            i = bisect_left(lst, limit) - 1
            return lst[i] if i >= 0 else -1

        # right0[i]: max index in word1 to match word2[i...] with 0 mismatches
        right0 = [-1] * (m + 1)
        right0[m] = n
        
        curr0 = n - 1
        for i in range(m - 1, -1, -1):
            curr0 = min(curr0, right0[i + 1] - 1)
            while curr0 >= 0 and word1[curr0] != word2[i]:
                curr0 -= 1
            right0[i] = curr0

        # right1[i]: max index in word1 to match word2[i...] with <= 1 mismatch
        right1 = [-1] * (m + 1)
        right1[m] = n
        
        for i in range(m - 1, -1, -1):
            # Option A: Match word2[i] exactly, allowing <= 1 mismatch in suffix
            cand_a = get_last_less_than(word2[i], right1[i + 1])
            
            # Option B: Mismatch word2[i], requiring 0 mismatches in suffix
            cand_b = right0[i + 1] - 1 if right0[i + 1] != -1 else -1
            
            right1[i] = max(cand_a, cand_b)

        res = []
        idx = 0
        mismatch_used = False

        # Greedy forward pass to find lexicographically smallest sequence
        for i in range(m):
            if not mismatch_used:
                while idx < n:
                    if word1[idx] == word2[i]:
                        if idx < right1[i + 1]:
                            res.append(idx)
                            idx += 1
                            break
                    else:
                        if idx < right0[i + 1]:
                            res.append(idx)
                            mismatch_used = True
                            idx += 1
                            break
                    idx += 1
            else:
                while idx < n and word1[idx] != word2[i]:
                    idx += 1
                if idx < n:
                    res.append(idx)
                    idx += 1

            if len(res) <= i:
                return []

        return res