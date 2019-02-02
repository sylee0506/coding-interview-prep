def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack += graph[vertex] - set(visited)

    return visited

def BFS(graph, root):
    visited = []
    queue = [root]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue += graph[vertex] - set(visited)

    return visited

#testing
graph = {'A':set(['B','C']), 'B':set(['A','D','E']), 'C':set(['A','F']), 'D':set(['B']), 'E':set(['B','F']), 'F':set(['C','E'])}
print('DFS: ',DFS(graph, 'A'))
print('BFS: ',BFS(graph, 'A'))
