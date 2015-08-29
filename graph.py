#implementation of graph data structure
#using python dicts
#assuming we are implementing an unweighted *undirected* graph
#therefore if v1 has v2 in its list of adjacent vertices, v2 must have v1

class graph(object):

    def __init__(self, grph = None):
        #initialize with option to pre define a starting node

        if grph is None:
            self.g = {}
        elif type(grph) is int:
            self.g = {grph:[]}
        else:
            print("Vertex key must be an int")
        return

    def addVertex(self, val):
        #search dictionary keys for the vertex key
        #adding a vertex if it is not found
        #and printing a message if it is

        vertices = self.g.keys()

        if val in vertices:
            print("Vertex already exists")
        else:
            self.g[val]=[]
        return

    def addEdge(self, val1, val2):
        #search index for both vertices
        #if they are found, looks to see if edge already exists
        #if no edge exists, create one, otherwise prints error

        vertices = self.g.keys()

        if (val1 in vertices) and (val2 in vertices):
            if val2 in self.g[val1]:
                print("Edge already exists")
            else:
                #make sure to add the 'edge' to both
                #vertices' lists
                self.g[val1].append(val2)
                self.g[val2].append(val1)
        else:
            print("One or more vertices not found")

        return

    def findVertex(self, val):
        #find a vertex and print its adjacent keys if found

        vertices = self.g.keys()

        if val in vertices:
            print "Adjacent Vertices: ", self.g[val]
        else:
            print("Vertex not found")

        return

