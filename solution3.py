import random

class Vertex:
    def __init__(self,name,degree=0):
        self.name = name
        self.degree = degree
    def getDegree(self):
        return self.degree
    def setDegree(self,deg):
        self.degree = deg
    def getName(self):
        return self.name

class Edge:
    def __init__(self,vertex1,vertex2):
        self.vertex1 = Vertex(vertex1)
        self.vertex2 = Vertex(vertex2)

class Graph:
    def __init__(self,size=None):#constructor
        if size < 0:
            raise Exception('Invalid size for graph')
        self.vertices = {}
        if not self.vertices:
            for i in range(size):
                self.addVertex(str(i+1))
        self.edges = []

        print("created graph ",end='')
        if self.vertices:
            print("with vertices :")
            print("{",end='')
            i=0
            for key, value in self.vertices.items():
                i+=1
                if i is not len(self.vertices):
                    print(key,",",end='')
                else:
                    print(key,end='')
                    print("}")
        else:
            print("\n")#end of constructor

    def verticesDoNotContain(self, vname):
        if vname in self.vertices:
            return False
        return True

    def addVertex(self,vname):
        if self.verticesDoNotContain(vname):
            new_vertex = Vertex(vname)
            self.vertices[vname]=new_vertex
            print("added vertex ",vname)
        else:
            raise Exception("vertex index must be unique!")

    def addMultipleVertices(self,names):
        for vname in names:
            self.addVertex(vname)

    def addThisManyVertices(self,number):#TODO For another time: there could be V={1,3,4} and len==3 but 4 already exists
        for i in range(number):
            self.addVertex(str(len(self.vertices)+1))

    def edgesDoNotContain(self,vname1,vname2):
        for edge in self.edges:
            if edge.vertex1.name == vname1 and edge.vertex2.name == vname2:
                return False
            if edge.vertex1.name == vname2 and edge.vertex2.name == vname1:
                return False
        return True

    def addEdge(self,vname1,vname2):
        if vname1 not in list(self.vertices.keys()) or vname2 not in list(self.vertices.keys()):
            raise ValueError('cannot add an edge between non existent vertices')
        if self.edgesDoNotContain(vname1,vname2):
            edge = Edge(vname1,vname2)
            self.edges.append(edge)
            self.vertices[vname1].setDegree(self.vertices[vname1].getDegree()+1)
            self.vertices[vname2].setDegree(self.vertices[vname2].getDegree()+1)
            #self.edges[-1].vertex1.setDegree(self.edges[-1].vertex1.getDegree()+1)
            #self.edges[-1].vertex2.setDegree(self.edges[-1].vertex1.getDegree()+1)
            print("added edge [", edge.vertex1.name,",",edge.vertex2.name,"]")
        else:
            print("the edge ",vname1,vname2," already exists")

    def addEdgesRandomly(self):
        print("Adding edges randomly")
        temp_list = list(self.vertices.keys())
        for key1, value1 in self.vertices.items():
            for key2 in temp_list:
                toAddOrNotToAdd = bool(random.getrandbits(1))
                if toAddOrNotToAdd == False:
                    if value1.name is not self.vertices[key2].name and self.edgesDoNotContain(key1,key2):
                        print("decided not to add the [",key1,",",key2,"] edge")
                if toAddOrNotToAdd:
                    if value1.name is not self.vertices[key2].name and self.edgesDoNotContain(key1,key2):
                        self.addEdge(key1,key2)
            temp_list.remove(key1)
    def displayDegreeSequence(self):
        print("degree sequence:")
        print("Vertex  |  degree")
        for key, value in self.vertices.items():
            print(value.name,"         ",end='')
            #print('%5s' % element.name,end='')
            print(self.vertices[key].getDegree())

g = Graph(2)
g.addVertex('3')
g.addEdge('2','3')
g.addThisManyVertices(2)
g.addEdgesRandomly()
g.displayDegreeSequence()
g.addThisManyVertices(1)
g.addEdgesRandomly()
g.displayDegreeSequence()
