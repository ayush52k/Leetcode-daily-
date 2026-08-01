from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequency of each character
        freq = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        # Step 3: Calculate pushes based on position rank
        for i, count in enumerate(sorted_freqs):
            pushes_per_char = (i // 8) + 1
            total_pushes += count * pushes_per_char
            
        return total_pushes