NodeData = {
    "A": ["B", "C"],
    "B": ["D", "E", "A"],
    "C": ["F", "G", "A"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "H", "E"],
    "G": ["C"],
    "H": ["F"]
}


# CLASS FOR NODE OBJECT
class Node:
    def __init__(self, data, children) -> None:
        self.data = data
        self.children = children

nodes = []

# ADDING NODES TO THE GRAPH
for node in NodeData:
    new = None
    if NodeData[node]:
        new = Node(
            data=node,
            children=NodeData[node]
        )
    else:
        new = Node(
            data=node,
            children=None
        )
    nodes.append(new)

open = nodes
waiting = [None]
visited = []

# TERMINATION DATA
start = input("Enter start node: ").upper()
goal = input("Enter end node: ").upper()
currentNode = Node(data=None, children=None) #PLACEHOLDER NODE

# CHECKING IF START NODE EXISTS
if start not in NodeData:
    print("Start node doesn't exist")
    exit

# GET THE NEW NODE TO WORK WITH
for node in open:
    if node.data == start:
        waiting.append(node)
        open.remove(node)

# TRAVERSING THE GRAPH
while currentNode:
    if currentNode.data == goal:
        # insert at top
        visited.append(currentNode)
        break
    else:
        # ADDING THE CURRENT NODE TO THE VISITED STACK
        visited.append(currentNode)
        # NOW ADDING CHILDREN OF CURRENTNODE
        # TO WAITING
        if currentNode.children:
            for child in currentNode.children:
                for node in open:
                    if node.data == child:
                        waiting.append(node)
                        open.remove(node)

        currentNode = waiting.pop()

# REMOVING THE PLACEHOLDER NODE
visited = visited[1:]

# ROUTINE TO CHECK IF AN ARRAY CONTAINS
# ANY OF ITS ELEMENTS IN ANOTHER ARRAY
def subCheck(arr1, arr2):
    flag = False
    for i in arr1:
        if i in arr2:
            flag = True
    return flag

# ROUTINE TO REMOVE NODE FROM AN ARRAY
# RETURNS THE NEW ARRAY
def removeNode(node, array):
    for n in array:
        if node.data == n.data:
            array.remove(node)
    return array

# TRACING BACK THE PATH FROM START NODE TO GOAL NODE
visitedCopy = visited[:]

for i in range(len(visitedCopy)):
    node = visitedCopy[i]
    subVisitedData = [chnode.data for chnode in visitedCopy[i+1:]]
    if not subCheck(node.children, subVisitedData):
        if node.data != goal:
            visited = removeNode(node, visited)

if visited[-1].data == goal:
    print("Goal node reached!")
    # THE PATH FROM START NODE TO GOAL NODE
    for node in visited:
        print(node.data)
else:
    print("Goal doesn't exist.")
