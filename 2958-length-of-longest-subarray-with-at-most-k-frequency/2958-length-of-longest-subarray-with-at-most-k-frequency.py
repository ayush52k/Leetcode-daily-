from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Expand window by including nums[right]
            count[nums[right]] += 1

            # Shrink window from the left if nums[right] exceeds allowed frequency k
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            # Update maximum length found so far
            max_length = max(max_length, right - left + 1)

        return max_length