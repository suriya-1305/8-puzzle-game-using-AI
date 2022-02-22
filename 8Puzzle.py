class Node:
    def __init__(s,data,level,fval):
        s.data = data
        s.level = level
        s.fval = fval
    def generate_child(s):
        x,y = s.find(s.data,'_')
        valList = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in valList:
            child = s.shuffle(s.data,x,y,i[0],i[1])
            if child is not None:
                childnode = Node(child,s.level+1,0)
                children.append(childnode)
        return children        
    def shuffle(s,puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(s.data) and y2 >= 0 and y2 < len(s.data):
            tpuz = []
            tpuz = s.copy(puz)
            temp = tpuz[x2][y2]
            tpuz[x2][y2] = tpuz[x1][y1]
            tpuz[x1][y1] = temp
            return tpuz
        else:
            return None
    def copy(s,root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp                
    def find(s,puz,x):
        for i in range(0,len(s.data)):
            for j in range(0,len(s.data)):
                if puz[i][j] == x:
                    return i,j

class Puzzle:
    def __init__(s,size):
        s.n = size
        s.open = []
        s.closed = []
    def accept(s):
        puz = []
        for i in range(0,s.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz
    def f(s,start,goal):
        return s.h(start.data,goal)+start.level
    def h(s,start,goal):
        temp = 0
        for i in range(0,s.n):
            for j in range(0,s.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
    def process(s):
        print("Enter the start state matrix \n")
        start = s.accept()
        print("Enter the goal state matrix \n")        
        goal = s.accept()
        start = Node(start,0,0)
        start.fval = s.f(start,goal)
        s.open.append(start)
        print("\n\n")
        while True:
            cur = s.open[0]
            print("")
            print("next Move \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            if(s.h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = s.f(i,goal)
                s.open.append(i)
            s.closed.append(cur)
            del s.open[0]
            s.open.sort(key = lambda x:x.fval,reverse=False)

puz = Puzzle(3)
puz.process()
