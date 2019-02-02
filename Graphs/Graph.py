class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.key) + 'connected to: ' + str([x.key for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getKey(self):
        return self.key

    def getWeight(self, nbr):
        if nbr in self.connectedTo:
            return self.connectedTo[nbr]
        else:
            return None

        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        new = Vertex(key)
        self.vertList[key] = new
        return new

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

#testing
g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
print(g.getVertices())
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    print(v.getConnections())
    print(v.getWeight(g.getVertex(5)))
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getKey(), w.getKey()))
