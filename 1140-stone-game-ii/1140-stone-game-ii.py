from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Build suffix sums where suffix_sum[i] is sum(piles[i:])
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            # If current player can take all remaining piles, take them all
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            # Find the minimum score the opponent can get
            min_opponent_score = float('inf')
            for X in range(1, 2 * M + 1):
                min_opponent_score = min(min_opponent_score, dp(i + X, max(M, X)))
                
            return suffix_sum[i] - min_opponent_score

        return dp(0, 1)