class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        nxt = head.next.next
        
        first_idx = -1
        last_idx = -1
        min_dist = float('inf')
        
        idx = 1
        
        while nxt:
            is_max = curr.val > prev.val and curr.val > nxt.val
            is_min = curr.val < prev.val and curr.val < nxt.val
            
            if is_max or is_min:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - last_idx)
                
                last_idx = idx
                
            prev = curr
            curr = nxt
            nxt = nxt.next
            idx += 1
            
        if first_idx == -1 or first_idx == last_idx:
            return [-1, -1]
            
        return [min_dist, last_idx - first_idx]