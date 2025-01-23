# islands

def count_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # All 8 directions

    def dfs(x, y):
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] == 1:
                dfs(nx, ny)

    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                island_count += 1  # New island found
                dfs(i, j)  # Mark the entire island

    return island_count

matrix = [
         [1, 1, 0, 0 ,0],
         [0 ,1, 0 ,0 ,1],
         [1 ,0, 0, 1, 1],
         [0, 0 ,0 ,0 ,0],
         [1, 0, 1, 0, 1]]

print(f"the number of islands is: {count_islands(matrix)}")
