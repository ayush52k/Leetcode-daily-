from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        # Extract coordinates of 1s for both images
        A = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        B = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count frequency of each translation vector (dr, dc)
        shift_counts = defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in A:
            for r2, c2 in B:
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] += 1
                max_overlap = max(max_overlap, shift_counts[shift])
                
        return max_overlap