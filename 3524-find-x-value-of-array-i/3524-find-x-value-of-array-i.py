class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            val = num % k
            next_dp = [0] * k
            
            # Subarray consisting of just the current element
            next_dp[val] += 1
            
            # Extend existing subarrays ending at the previous element
            for rem in range(k):
                if dp[rem] > 0:
                    next_dp[(rem * val) % k] += dp[rem]
            
            # Accumulate counts into the global result
            for rem in range(k):
                result[rem] += next_dp[rem]
                
            dp = next_dp

        return result