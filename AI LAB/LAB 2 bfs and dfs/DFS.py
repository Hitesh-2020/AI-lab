def dfs(adj_list, start, target, path, visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in adj_list[start]:
        if neighbour not in visited:
            result = dfs(adj_list, neighbour, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None



# adj_list = {'A': ['B', 'E', 'C'],
# 			'B': ['A', 'D', 'E'],
# 			'C': ['A', 'F', 'G'],
# 			'D': ['B', 'E'],
# 			'E': ['A', 'B', 'D'],
# 			'F': ['C'],
# 			'G': ['C']}

            
adj_list = {"A": ["B", "C"],
    "B": ["D", "E", "A"],
    "C": ["F", "G", "A"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "H", "E"],
    "G": ["C"],
    "H": ["F"]
}


traversal_path = []
traversal_path = dfs(adj_list, 'B', 'H', traversal_path)
print(traversal_path)