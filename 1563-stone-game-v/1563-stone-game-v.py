class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
            
        # Prefix sums for O(1) range sum lookups
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]

        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]

        # Base cases initialization for length 1
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        # mid_ptr[i] stores the largest split point for an interval starting at i 
        # where the left sum is <= the right sum.
        mid_ptr = [i - 1 for i in range(n)]

        # Evaluate lengths from 2 up to N
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Two-pointer optimization: advance mid_ptr[i] in O(1) amortized time
                while mid_ptr[i] + 1 < j and get_sum(i, mid_ptr[i] + 1) <= get_sum(mid_ptr[i] + 2, j):
                    mid_ptr[i] += 1
                
                mid = mid_ptr[i]
                ans = 0

                # 1. Left sum <= Right sum
                if mid >= i:
                    if get_sum(i, mid) == get_sum(mid + 1, j):
                        # L == R: Alice gets to pick between the optimal left or optimal right
                        if mid > i:
                            ans = max(ans, max_l[i][mid - 1]) # Best strictly left choices
                        
                        # Compare the exact midpoint choices explicitly
                        ans = max(ans, 
                                  get_sum(i, mid) + dp[i][mid], 
                                  get_sum(mid + 1, j) + dp[mid + 1][j])
                    else:
                        # L < R: Bob forces Alice left
                        ans = max(ans, max_l[i][mid])

                # 2. Left sum > Right sum (for all split points past 'mid')
                # Bob forces Alice right
                if mid + 2 <= j:
                    ans = max(ans, max_r[mid + 2][j])

                dp[i][j] = ans

                # Update the auxiliary DP maximum arrays for the current [i, j]
                total = get_sum(i, j)
                max_l[i][j] = max(max_l[i][j - 1], total + dp[i][j])
                max_r[i][j] = max(max_r[i + 1][j], total + dp[i][j])

        return dp[0][n - 1]