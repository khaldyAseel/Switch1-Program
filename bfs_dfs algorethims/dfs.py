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

print(dfs_sum(number_graph,3))


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

print(dfs_odd(number_graph,3))


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
#       