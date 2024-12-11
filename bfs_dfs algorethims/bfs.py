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

def sum_bfs(graph,node,visited=None):
    visited = [] 
    queue = []
    sum = 0   
    
    visited.append(node)
    queue.append(node)
    sum+=node
    while queue:
        node = queue.pop(0) 
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                sum+=neighbour

    return sum

print(sum_bfs(number_graph,3))


def primes_bfs(graph,node,visited=None):
    visited = [] 
    queue = []
    sum = 0   
    
    visited.append(node)
    queue.append(node)
    if is_prime(node):
        sum+=node
    while queue:
        node = queue.pop(0) 
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            if is_prime(neighbour):
                sum+=neighbour

    return sum

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(primes_bfs(number_graph,3))