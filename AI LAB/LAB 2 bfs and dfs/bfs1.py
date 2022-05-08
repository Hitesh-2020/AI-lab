adj = {'A':['B','C'],'B':['D','E'],'C':['F','G'],'F':['H']}

path = {}

q = []
visit = []

def bfs(start,end):
    vnode = '0'

    q.append(start)
    
    while q != []:
        
        if q[0] == end:
            for vnode in adj:

        vnode = q.pop(0)
        visit.append(vnode)


        if(vnode == end)
            

        if vnode in adj.keys():
            for i in adj[vnode]:
                print(i)
                q.append(i)

bfs('A','H')
print(q)
print(visit)