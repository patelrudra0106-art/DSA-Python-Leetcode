from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        n, m = len(grid), len(grid[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        maxHealth = [[-1] * m for _ in range(n)]

        initialH = health - grid[0][0]
        if initialH <= 0:
            return False

        q = deque()
        q.append((initialH, 0, 0))
        maxHealth[0][0] = initialH

        while q:
            currH, r, c = q.popleft()

            if r == n - 1 and c == m - 1:
                return True

            for d in range(4):
                nr = r + dx[d]
                nc = c + dy[d]

                if nr < 0 or nc < 0 or nr >= n or nc >= m:
                    continue

                remH = currH - grid[nr][nc]

                if remH <= 0:
                    continue

                if remH <= maxHealth[nr][nc]:
                    continue

                maxHealth[nr][nc] = remH
                q.append((remH, nr, nc))

        return False