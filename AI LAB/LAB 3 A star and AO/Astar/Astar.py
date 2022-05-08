from timeit import default_timer

class Graph:
    f = []

    def __init__(self,adj,h = {}):
        self.adj_list = adj
        
        if h == {}:
            for i in adj:
                for j in adj[i]:
                    h[j[0]] = 1
            
        self.h = h
        

    def fninsert(self,cur):
        k = 0

        while k != len(Graph.f):
            if Graph.f[k][1][-1] == cur:
                temp = Graph.f.pop(k)

                for i in self.adj_list[cur]:
                    if i[0] not in temp[1]:
                        Graph.f.insert(k,[ (temp[0] - self.h[cur] + i[1] + self.h[i[0]]), temp[1] + (i[0],) ])
        
            k = k + 1


    def isExpandable(self,start,goal):
        # if min(Graph.f)[1][-1] == goal:
        #             return 2

        for path in Graph.f:
            if path[1][-1] != goal and path[1][-1] in self.adj_list:
                if len(self.adj_list[path[1][-1]]) != 1:
                    return 1
                elif self.adj_list[path[1][-1][0]][0] != start:
                    return 1
                else:
                    return 0

    def isPath(self,goal):
        for i in Graph.f:
            if i[1][-1] == goal:
                return 1

        return 0

    def astar(self,start,goal):
        stTime = default_timer()

        Graph.f.clear()
        
        flag = 1

        if start not in self.adj_list:
            flag = 0
          
        self.h[goal] = 0
        
        while flag == 1:

            if Graph.f == []:
                for i in self.adj_list[start]:
                    Graph.f.append([i[1] + self.h[i[0]], (start,i[0])])
            else:
                for i in Graph.f:
                    # minfn = min(Graph.f)

                    # if i[1][-1] != goal and minfn == i:
                    if i[1][-1] != goal:
                        self.fninsert(i[1][-1])
                    
                flag = self.isExpandable(start,goal)
                      

        if self.isPath(goal) == 1:
            print(f'Optimal Path from {start} to {goal}: {min(Graph.f)[1]} with Path COST: {min(Graph.f)[0]}')
        else:
            print('\n!!Path not possible!!')

        print('\nTime Complexity =',default_timer()-stTime)
        
        # print(Graph.f)  

        



adj_list = {'S':[('A',1),('B',2)],
            'A':[('Y',7),('X',4)],
            'B':[('C',7),(('D',1))],
            'Y':[('E',3)],
            'X':[('E',2)],
            'C':[('E',5)],
            'D':[('E',12)]
            }

h = {'A':5,
     'B':6,
     'C':4,
     'D':15,
     'X':5,
     'Y':8
    }

# adj_list = {
#     'A': [('B', 1), ('C', 3), ('D', 7)],
#     'B': [('D', 5)],
#     'C': [('D', 12)]
# }


# adj_list = {'S':[('B',4),('C',3)],
#             'B':[('E',12),('F',5)],
#             'C':[('D',7),('E',10)],
#             'D':[('E',2)],
#             'E':[('G',5)],
#             'F':[('G',16)]
# }

# h = {'S':14,
#      'B':12,
#      'C':11,
#      'D':6,
#      'E':4,
#      'F':11
# }


# adj_list = {
#     'A': [('B', 6), ('F', 3)],
#     'B': [('A', 6), ('C', 1), ('D', 2)],
#     'C': [('B', 3), ('D', 1), ('E', 1)],
#     'D': [('B', 2), ('C', 1), ('E', 8)],
#     'E': [('C', 5), ('D', 8), ('I', 5), ('J', 1)],
#     'F': [('A', 3), ('G', 1), ('H', 7)],
#     'G': [('F', 1), ('I', 3)],
#     'H': [('F', 7), ('I', 2)],
#     'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
# }

# h = {
#         'A': 11,
#         'B': 8,
#         'C': 5,
#         'D': 7,
#         'E': 3,
#         'F': 6,
#         'G': 5,
#         'H': 3,
#         'I': 1,
#         'J': 0
#     }

# adj_list = {
#     'A': [('B', 20), ('E', 3)],
#     'B': [('A', 2), ('C', 1), ('G', 9)],
#     'C': [('B', 1)],
#     'D': [('E', 6), ('G', 1)],
#     'E': [('A', 3), ('D', 6)],
#     'G': [('B', 9), ('D', 1)]
# }

# h = {
#         'A': 11,
#         'B': 6,
#         'C': 99,
#         'D': 1,
#         'E': 7,
#         'G': 0,
#     }

g = Graph(adj_list,h)

g.astar('S','E')