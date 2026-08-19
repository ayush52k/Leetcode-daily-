from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        modified_rows = defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                modified_rows[row].add(seat)
                
        ans = (n - len(modified_rows)) * 2
        
        for row, seats in modified_rows.items():
            left_free = not any(s in seats for s in (2, 3, 4, 5))
            right_free = not any(s in seats for s in (6, 7, 8, 9))
            middle_free = not any(s in seats for s in (4, 5, 6, 7))
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or middle_free:
                ans += 1
                
        return ans