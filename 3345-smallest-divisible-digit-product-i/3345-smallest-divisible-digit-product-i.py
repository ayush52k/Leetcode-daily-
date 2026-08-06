class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        x = n
        while True:
            prod = 1
            for digit in str(x):
                prod *= int(digit)
                
            if prod % t == 0:
                return x
                
            x += 1