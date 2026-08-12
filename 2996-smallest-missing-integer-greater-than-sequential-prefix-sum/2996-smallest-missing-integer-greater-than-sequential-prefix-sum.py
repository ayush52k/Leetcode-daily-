class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Compute sum of the longest sequential prefix starting at index 0
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        # Step 2: Find smallest x >= prefix_sum not present in nums
        num_set = set(nums)
        while prefix_sum in num_set:
            prefix_sum += 1

        return prefix_sum