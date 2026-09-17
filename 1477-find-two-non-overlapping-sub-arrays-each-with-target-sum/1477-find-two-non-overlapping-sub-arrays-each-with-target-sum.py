class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        inf = float('inf')
        
        # min_len[i] stores the minimum length of a valid subarray ending at or before index i
        min_len = [inf] * n
        
        # Hash map to store prefix_sum -> index
        prefix_map = {0: -1}
        
        curr_sum = 0
        ans = inf
        best_so_far = inf  # Running minimum length of a valid subarray
        
        for i in range(n):
            curr_sum += arr[i]
            
            # Check if there exists a subarray ending at index i with sum equal to target
            if (curr_sum - target) in prefix_map:
                start_idx = prefix_map[curr_sum - target]
                curr_len = i - start_idx
                
                # If there is a valid non-overlapping subarray before start_idx + 1
                if start_idx >= 0 and min_len[start_idx] != inf:
                    ans = min(ans, curr_len + min_len[start_idx])
                
                # Update best length seen so far
                best_so_far = min(best_so_far, curr_len)
            
            # Store the minimum length valid subarray seen up to index i
            min_len[i] = best_so_far
            prefix_map[curr_sum] = i
            
        return ans if ans != inf else -1