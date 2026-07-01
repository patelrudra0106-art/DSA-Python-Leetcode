class Solution:
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def maximumSafenessFactor(self, A: List[List[int]]) -> int:
        n = len(A)

        if A[0][0] or A[n - 1][n - 1]:
            return 0

        q = deque()

        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            v = A[i][j]

            for dx, dy in self.dirs:
                x, y = i + dx, j + dy

                if min(x, y) >= 0 and max(x, y) < n and not A[x][y]:
                    A[x][y] = v + 1
                    q.append((x, y))

        pq = [(-A[0][0], 0, 0)]

        while pq:
            sf, i, j = heapq.heappop(pq)
            sf = -sf

            if i == n - 1 and j == n - 1:
                return sf - 1

            for dx, dy in self.dirs:
                x, y = i + dx, j + dy

                if min(x, y) >= 0 and max(x, y) < n and A[x][y] > 0:
                    heapq.heappush(pq, (-min(sf, A[x][y]), x, y))
                    A[x][y] *= -1

        return A[n - 1][n - 1] - 1