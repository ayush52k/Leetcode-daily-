class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        depth = 0
        
        for char in seq:
            if char == '(':
                answer.append(depth % 2)
                depth += 1
            else:  # char == ')'
                depth -= 1
                answer.append(depth % 2)
                
        return answer