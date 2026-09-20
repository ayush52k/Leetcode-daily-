class Solution:

    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for i, char in enumerate(s, start=1):
            reversed_alphabet_pos = 26 - (ord(char) - ord('a'))
            total_degree += reversed_alphabet_pos * i
        return total_degree