class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        
        # Segment tree nodes represented as flat arrays for max performance
        tree_left_char = [''] * (4 * n)
        tree_right_char = [''] * (4 * n)
        tree_left_len = [0] * (4 * n)
        tree_right_len = [0] * (4 * n)
        tree_max_len = [0] * (4 * n)
        tree_length = [0] * (4 * n)

        def merge(node: int, lc: int, rc: int) -> None:
            tree_length[node] = tree_length[lc] + tree_length[rc]
            tree_left_char[node] = tree_left_char[lc]
            tree_right_char[node] = tree_right_char[rc]

            m_len = max(tree_max_len[lc], tree_max_len[rc])
            l_len = tree_left_len[lc]
            r_len = tree_right_len[rc]

            # Merge condition if character across boundary matches
            if tree_right_char[lc] == tree_left_char[rc]:
                m_len = max(m_len, tree_right_len[lc] + tree_left_len[rc])
                
                if tree_left_len[lc] == tree_length[lc]:
                    l_len = tree_length[lc] + tree_left_len[rc]
                if tree_right_len[rc] == tree_length[rc]:
                    r_len = tree_length[rc] + tree_right_len[lc]

            tree_max_len[node] = m_len
            tree_left_len[node] = l_len
            tree_right_len[node] = r_len

        def build(node: int, start: int, end: int) -> None:
            if start == end:
                c = s[start]
                tree_left_char[node] = c
                tree_right_char[node] = c
                tree_left_len[node] = 1
                tree_right_len[node] = 1
                tree_max_len[node] = 1
                tree_length[node] = 1
                return
            
            mid = (start + end) // 2
            lc, rc = 2 * node, 2 * node + 1
            build(lc, start, mid)
            build(rc, mid + 1, end)
            merge(node, lc, rc)

        def update(node: int, start: int, end: int, idx: int, ch: str) -> None:
            if start == end:
                tree_left_char[node] = ch
                tree_right_char[node] = ch
                tree_left_len[node] = 1
                tree_right_len[node] = 1
                tree_max_len[node] = 1
                tree_length[node] = 1
                return

            mid = (start + end) // 2
            lc, rc = 2 * node, 2 * node + 1
            if idx <= mid:
                update(lc, start, mid, idx, ch)
            else:
                update(rc, mid + 1, end, idx, ch)
            merge(node, lc, rc)

        # Build initial tree
        build(1, 0, n - 1)

        # Process queries
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree_max_len[1])

        return ans