from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        # Preserve original indices: [l, r, weight, id]
        sorted_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            sorted_intervals.append((l, r, w, i))
        
        # Sort intervals primarily by start time l
        sorted_intervals.sort(key=lambda x: x[0])
        
        # Array of start times for binary search
        starts = [x[0] for x in sorted_intervals]
        
        # dp[i][k] = (max_weight, sorted_list_of_indices)
        # using intervals from index i to n-1, picking up to k intervals
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        # Process backward from n-1 down to 0
        for i in range(n - 1, -1, -1):
            l_i, r_i, w_i, id_i = sorted_intervals[i]
            
            # Find the first interval starting strictly after current end time r_i
            next_idx = bisect_right(starts, r_i)
            
            for k in range(1, 5):
                # Option 1: Skip interval i
                best_weight, best_indices = dp[i + 1][k]
                
                # Option 2: Take interval i
                prev_weight, prev_indices = dp[next_idx][k - 1]
                cand_weight = w_i + prev_weight
                cand_indices = sorted([id_i] + prev_indices)
                
                # Compare Options
                if cand_weight > best_weight:
                    best_weight = cand_weight
                    best_indices = cand_indices
                elif cand_weight == best_weight and cand_weight > 0:
                    if cand_indices < best_indices:
                        best_indices = cand_indices
                
                dp[i][k] = (best_weight, best_indices)
                
        return dp[0][4][1]