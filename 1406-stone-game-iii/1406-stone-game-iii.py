class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] represents the max score difference for the player whose turn it is
        # Using a cyclic array of size 4 for O(1) space complexity
        dp = [0] * 4
        
        for i in range(n - 1, -1, -1):
            max_diff = float('-inf')
            current_take = 0
            
            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    current_take += stoneValue[i + k - 1]
                    max_diff = max(max_diff, current_take - dp[(i + k) % 4])
                    
            dp[i % 4] = max_diff
            
        alice_diff = dp[0]
        
        if alice_diff > 0:
            return "Alice"
        elif alice_diff < 0:
            return "Bob"
        else:
            return "Tie"