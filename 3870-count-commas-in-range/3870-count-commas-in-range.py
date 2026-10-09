class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        start = 1000
        commas_per_num = 1
        
        while start <= n:
            next_start = start * 1000
            # Count numbers in range [start, min(n, next_start - 1)]
            count = min(n, next_start - 1) - start + 1
            total_commas += count * commas_per_num
            
            start = next_start
            commas_per_num += 1
            
        return total_commas