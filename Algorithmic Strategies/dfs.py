number_graph = {
    3:[1,5,8],
    4: [2],
    1: [9,6],
    5: [],
    8: [7],
    7:[4],
    9: [],
    6:[],
    2: []
}

def dfs_sum(graph,node,visited=None):
    sum = 0 
    if visited is None:
        visited = []
    if node not in visited:
        sum+=node
        visited.append(node)
    for neighbour in graph[node]:
        sum += dfs_sum(graph,neighbour,visited)

    return sum

print(f"sum of nums:{dfs_sum(number_graph,3)}")


def dfs_odd(graph,node,visited=None):
    sum = 0 
    if visited is None:
        visited = []
    if node not in visited:
        sum+=node
        visited.append(node)
    for neighbour in graph[node]:
        if neighbour%2 ==1:
            sum += dfs_odd(graph,neighbour,visited)

    return sum

print(f"sum of odd nums: {dfs_odd(number_graph,3)}")


maze1 = [
    [2, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 3, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0]
]


# to transform the maze to tree 
#   1. insert root
#   2. look for the next index 
#       if 1: 
#       insert node 
#       else : pass

def dfs_find_path(maze):
    rows, cols = len(maze), len(maze[0])

    # Find the start (2) and end (3) positions
    start = None
    goal = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                goal = (i, j)

    if not start or not goal:
        return []  # Either start or goal is missing, return empty path

    visited = set()

    # Depth-First Search to find the path
    def dfs(x, y, path):
        # Add the current cell to the path
        path.append((x, y))
        visited.add((x, y))

        # If we reach the goal, return True and keep the path
        if (x, y) == goal:
            return True

        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check boundaries and if the cell is valid
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if maze[nx][ny] == 1 or maze[nx][ny] == 3:  # Can move through 1 or to the goal
                    if dfs(nx, ny, path):
                        return True

        # Backtrack if no path is found from this cell
        path.pop()
        return False

    # Start DFS from the start point and collect the path
    path = []
    if dfs(start[0], start[1], path):
        return path
    else:
        return []  # No path found


maze1 = [
    [2, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 3, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0]
]

# print the (x,y) of the path 
print(f"Path from 2 to 3:{dfs_find_path(maze1)}")

