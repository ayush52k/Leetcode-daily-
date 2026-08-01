class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        memo = {}

        def max_score_diff(left: int, right: int) -> int:
            # Base case: only one element left
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            # Option 1: Pick left element, subtract opponent's best response from nums[left+1 ... right]
            pick_left = nums[left] - max_score_diff(left + 1, right)
            
            # Option 2: Pick right element, subtract opponent's best response from nums[left ... right-1]
            pick_right = nums[right] - max_score_diff(left, right - 1)
            
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        # Player 1 wins if the score difference is >= 0
        return max_score_diff(0, len(nums) - 1) >= 0