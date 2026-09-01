from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_map = {}
        litter_count = 0
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1

        target_mask = (1 << litter_count) - 1
        
        if target_mask == 0:
            return 0

        # queue entries: (r, c, remaining_energy, collected_mask, steps)
        queue = deque([(start_r, start_c, energy, 0, 0)])
        
        # Tracks max remaining energy for state (r, c, mask)
        visited = {}
        visited[(start_r, start_c, 0)] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, e, mask, steps = queue.popleft()

            if mask == target_mask:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    new_e = e - 1
                    if new_e < 0:
                        continue  # Out of energy

                    cell = classroom[nr][nc]
                    new_mask = mask

                    if cell == 'R':
                        new_e = energy
                    elif cell == 'L':
                        litter_idx = litter_map[(nr, nc)]
                        new_mask |= (1 << litter_idx)

                    state_key = (nr, nc, new_mask)
                    if state_key in visited and visited[state_key] >= new_e:
                        continue

                    visited[state_key] = new_e
                    queue.append((nr, nc, new_e, new_mask, steps + 1))

        return -1