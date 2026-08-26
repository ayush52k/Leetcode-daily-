class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones_indices = [i for i, ch in enumerate(s) if ch == '1']
        
        if len(ones_indices) < k:
            return ""
        
        min_len = float('inf')
        best_sub = ""
        
        for j in range(len(ones_indices) - k + 1):
            start = ones_indices[j]
            end = ones_indices[j + k - 1]
            
            substring = s[start : end + 1]
            length = len(substring)
            
            if length < min_len:
                min_len = length
                best_sub = substring
            elif length == min_len:
                if substring < best_sub:
                    best_sub = substring
                    
        return best_sub