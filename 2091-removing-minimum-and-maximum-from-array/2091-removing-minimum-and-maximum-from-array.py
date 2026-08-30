class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        option_left = j + 1
        option_right = n - i
        option_both = (i + 1) + (n - j)

        return min(option_left, option_right, option_both)