import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Remove redundant coins (e.g., remove 6 if 3 is already present)
        coins = sorted(coins)
        filtered_coins = []
        for c in coins:
            if not any(c % existing == 0 for existing in filtered_coins):
                filtered_coins.append(c)
        
        n = len(filtered_coins)
        
        # Precompute LCM and sign (+1 / -1) for all non-empty subsets
        subsets = []
        for mask in range(1, 1 << n):
            lcm_val = 1
            bits = 0
            for i in range(n):
                if (mask >> i) & 1:
                    bits += 1
                    lcm_val = math.lcm(lcm_val, filtered_coins[i])
            sign = 1 if bits % 2 == 1 else -1
            subsets.append((lcm_val, sign))
        
        def count_multiples(X: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (X // lcm_val)
            return total

        # Binary search for the kth value
        low = 1
        high = min(filtered_coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans