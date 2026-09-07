class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Stores the count of new subsequences added when each character was last processed
        last = {}
        
        # total represents the count of distinct non-empty subsequences
        total = 0
        
        for char in s:
            # New subsequences formed by appending `char` to all current subsequences + 1 (for `char` alone)
            new_subsequences = (total + 1) % MOD
            
            # Remove duplicate counts from the previous occurrence of `char`
            added = (new_subsequences - last.get(char, 0)) % MOD
            
            # Update total and record how many new subsequences were contributed by `char`
            total = (total + added) % MOD
            last[char] = new_subsequences

        return total