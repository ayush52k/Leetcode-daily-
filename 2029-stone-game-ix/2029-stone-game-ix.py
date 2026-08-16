class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt0 = sum(1 for x in stones if x % 3 == 0)
        cnt1 = sum(1 for x in stones if x % 3 == 1)
        cnt2 = sum(1 for x in stones if x % 3 == 2)
        
        # If cnt0 is even, Alice wins if both cnt1 and cnt2 are non-zero
        if cnt0 % 2 == 0:
            return cnt1 > 0 and cnt2 > 0
        
        # If cnt0 is odd, Alice wins if the absolute difference between cnt1 and cnt2 is greater than 2
        return abs(cnt1 - cnt2) > 2    