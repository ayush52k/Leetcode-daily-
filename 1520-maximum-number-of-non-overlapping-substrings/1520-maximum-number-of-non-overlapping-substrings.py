class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find first and last occurrence of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        # Step 2: Try to form a valid substring starting at first[ch] for each character
        for ch in first:
            start = first[ch]
            end = last[ch]
            is_valid = True
            
            i = start
            while i <= end:
                # If a character inside starts before our start point, discard this start
                if first[s[i]] < start:
                    is_valid = False
                    break
                # Extend right endpoint if needed
                end = max(end, last[s[i]])
                i += 1

            if is_valid:
                valid_intervals.append((start, end))

        # Step 3: Sort valid intervals by end index (greedy interval scheduling)
        valid_intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for start, end in valid_intervals:
            if start > prev_end:
                ans.append(s[start : end + 1])
                prev_end = end

        return ans