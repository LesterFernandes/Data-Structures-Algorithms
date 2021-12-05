import collections

def numIslands(grid: list[list[str]]) -> int:
    ROWZ = len(grid)
    COLZ = len(grid[0])
    seen = set()
    islCount = 0

    def bfs(r, c):
        q = collections.deque()
        q.append((r, c))
        dirz = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            ro, co = q.popleft()
            seen.add((ro, co))
            for dr, dc in dirz:
                row = ro + dr
                col = co + dc
                if row in range(ROWZ) and col in range(COLZ) and (row, col) not in seen and grid[row][col] == '1':
                    q.append((row, col))

    for r in range(ROWZ):
        for c in range(COLZ):
            if grid[r][c] == '1' and (r, c) not in seen:
                bfs(r, c)
                islCount += 1

    return islCount

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# print(numIslands(grid))

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# print(numIslands(grid2))