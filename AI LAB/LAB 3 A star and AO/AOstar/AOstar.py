from timeit import default_timer

class andOrGraph:
    def __init__(self,adj,h):
        self.adj_list = adj
        self.h = h
        self.fn = []

    def fnInsert(self,cur):
            k = 0

            while k != len(self.fn):
                if len(self.fn[k][0]) == 1 and self.fn[k][0][0] == cur:
                    temp = self.fn.pop(k)
                    for i in self.adj_list[cur[-1]]:
                        self.fn.insert( k, [ [temp[0][0]+(i[0][0],)],temp[1] - self.h[temp[0][0][-1]] + i[0][1] + self.h[i[0][0]] ] )
                
                elif len(self.fn[k][0]) == 2 and self.fn[k][0][0] == cur:
                    temp = self.fn.pop(k)
                    for i in self.adj_list[cur[-1]]:
                        self.fn.insert( k, [ [temp[0][0]+(i[0][0],), temp[0][1]],temp[1] - self.h[temp[0][0][-1]] + i[0][1] + self.h[i[0][0]] ] )
                
                elif len(self.fn[k][0]) == 2 and self.fn[k][0][1] == cur:
                    temp = self.fn.pop(k)
                    for i in self.adj_list[cur[-1]]:
                        self.fn.insert( k, [ [temp[0][0], temp[0][1]+(i[0][0],)],temp[1] - self.h[temp[0][1][-1]] + i[0][1] + self.h[i[0][0]] ] )
    
                k = k + 1

    def isExpansionPossible(self):
        for i in self.fn:
            if len(i[0]) == 1 and ( h[i[0][0][-1]] == 0 or i[0][0][-1] not in self.adj_list ):
                # print('hell')
                print(i)
                return 0
            elif len(i[0]) == 2 and ( h[i[0][1][-1]] == 0 or ( i[0][0][-1] not in self.adj_list and i[0][1][-1] not in self.adj_list ) ):
                # print('WEll')
                print(i)

                return 0

        return 1

    def aoStar(self,start):
        stTime = default_timer()

        flag = 1

        while flag == 1:
            if self.fn == []:
                for i in self.adj_list[start]:
                    if len(i) == 1:
                        self.fn.append( [ [(start,i[0][0])], i[0][1]+self.h[i[0][0]] ] )
                    else:
                        self.fn.append( [ [(start,i[0][0]),(start,i[1][0])], (i[0][1]+self.h[i[0][0]] + i[1][1]+self.h[i[1][0]]) ] )
                # self.h[start] = min(self.fn, key = lambda x:x[1])[1]

            else:
                
                minfn = min(self.fn, key = lambda x:x[1])

                if (self.h[minfn[0][0][-1]] != 0 and minfn[0][0][-1] in self.adj_list):
                    self.fnInsert(minfn[0][0])
                elif (self.h[minfn[0][1][-1]] != 0 and minfn[0][1][-1] in self.adj_list):
                    self.fnInsert(minfn[0][1])
            
            # print(self.fn)
            # print(self.h)

            flag = self.isExpansionPossible()
            
            if flag == 0:
                print('\nTime Complexity =',default_timer()-stTime)


# adj_list = {
#     'A':[[('B',4),('C',5)],[('D',5)]],
#     'B':[[('C',2)]],
#     'C':[[('E',2)]],
#     'D':[[('E',2)],[('F',4)]],
#     'E':[[('F',3)]]
# }

# h = {
#     'A':8,
#     'B':1,
#     'C':2,
#     'D':8,
#     'E':1,
#     'F':0
# }

adj_list = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}

h = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}

g = andOrGraph(adj_list,h)

g.aoStar('A')
