from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        max_val = 100000
        count = [0] * (max_val + 1)
        
        # Step 1: Calculate absolute differences and store their frequencies
        total_diff = 0
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            count[diff] += 1
            total_diff += diff
            
        # If total operations can cover all differences, the minimum sum is 0
        k = k1 + k2
        if total_diff <= k:
            return 0
            
        # Step 2: Greedily reduce the largest differences
        for v in range(max_val, 0, -1):
            if count[v] > 0:
                # Number of operations needed to reduce count[v] items from v to v-1
                reduction = min(k, count[v])
                k -= reduction
                count[v] -= reduction
                count[v - 1] += reduction
                
                if k == 0:
                    break
                    
        # Step 3: Calculate the final sum of squared differences
        ans = 0
        for v in range(1, max_val + 1):
            if count[v] > 0:
                ans += count[v] * (v * v)
                
        return ans