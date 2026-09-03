class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Find the minimum odd number in the array
        min_odd = float('inf')
        for x in nums1:
            if x % 2 != 0:
                min_odd = min(min_odd, x)
        
        # If no odd numbers exist, all numbers are already even
        if min_odd == float('inf'):
            return True
        
        # Check if any even number is smaller than the smallest odd number
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
                
        return True