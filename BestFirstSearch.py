class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    def connect(self, A, B, dist=1):
        self.graph_dict.setdefault(A, {})[B] = dist
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = dist
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
class Node:
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
         return self.f < other.f
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
def BestFirstSearch(graph, heuristic, start, end):
    open = []
    closed = []
    snode = Node(start, None)
    gnode = Node(end, None)
    open.append(snode)
    while len(open) > 0:
        open.sort()
        cnode = open.pop(0)
        closed.append(cnode)        
        if cnode == gnode:
            path = []
            while cnode != snode:
                path.append(cnode.name + ': ' + str(cnode.g))
                cnode = cnode.parent
            path.append(snode.name + ': ' + str(snode.g))
            return path[::-1]
        neighbors = graph.get(cnode.name)
        for key, value in neighbors.items():
            neighbor = Node(key, cnode)
            if(neighbor in closed):
                continue
            neighbor.g = cnode.g + graph.get(cnode.name, neighbor.name)
            neighbor.h = heuristic.get(neighbor.name)
            neighbor.f = neighbor.h
            if(addToList(open, neighbor) == True):
                open.append(neighbor)
    return None
def addToList(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
if __name__ == '__main__':
    graph = Graph()
    graph.connect('a','b',9)
    graph.connect('a','c',4)
    graph.connect('a','d',7)
    graph.connect('b','e',11)
    graph.connect('c','e',17)
    graph.connect('c','f',12)
    graph.connect('d','f',14)
    graph.connect('f','z',9)
    graph.connect('e','z',5)
    graph.make_undirected()
    heuristic = {}
    heuristic['a']=21
    heuristic['b']=14
    heuristic['c']=18
    heuristic['d']=18
    heuristic['e']=5
    heuristic['f']=8
    heuristic['z']=0
    path=BestFirstSearch(graph, heuristic, 'a', 'z')
    print(path)
    
