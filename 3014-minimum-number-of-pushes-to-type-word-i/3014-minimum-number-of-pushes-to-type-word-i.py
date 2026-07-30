class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushes = 0
        
        # First 8 distinct characters take 1 push
        pushes += min(n, 8) * 1
        
        # Next 8 characters take 2 pushes
        if n > 8:
            pushes += min(n - 8, 8) * 2
            
        # Next 8 characters take 3 pushes
        if n > 16:
            pushes += min(n - 16, 8) * 3
            
        # Remaining characters take 4 pushes
        if n > 24:
            pushes += (n - 24) * 4
            
        return pushes

        