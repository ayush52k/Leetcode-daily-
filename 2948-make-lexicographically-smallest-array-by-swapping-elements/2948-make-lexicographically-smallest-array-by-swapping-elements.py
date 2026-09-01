from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Pair each number with its original index and sort by value
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        # Result array to store the optimal permutation
        result = [0] * n
        
        i = 0
        while i < n:
            j = i + 1
            # Expand current group as long as adjacent diff <= limit
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1
            
            # The range [i, j-1] forms one connected component
            # Values are already sorted in ascending order
            values = [sorted_pairs[k][0] for k in range(i, j)]
            # Get original indices and sort them to assign smallest values to earliest indices
            indices = sorted(sorted_pairs[k][1] for k in range(i, j))
            
            # Place values back into their original positions in sorted index order
            for val, orig_idx in zip(values, indices):
                result[orig_idx] = val
                
            i = j
            
        return result