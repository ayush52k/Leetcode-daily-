from collections import defaultdict

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subarray_counts = defaultdict(int)
        
        # Iterate over all subarrays of size k
        for i in range(n - k + 1):
            window = set(nums[i : i + k])  # Unique elements in current window
            for num in window:
                subarray_counts[num] += 1
                
        # Find the maximum element that appears in exactly 1 subarray
        ans = -1
        for num, count in subarray_counts.items():
            if count == 1:
                ans = max(ans, num)
                
        return ans