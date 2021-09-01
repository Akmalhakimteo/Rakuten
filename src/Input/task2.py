import math
from flask import Flask
from flask import request

def getMinDistance(fromNode,toNode,listthis,pathDict):
    for key,val in pathDict.items():
        if(fromNode==toNode):
            listthis.append(fromNode)
            # print("CUURRENT BEFORE",listthis)
            # print("CUURRENT STUFF",listthis[::-1])
            return listthis[::-1]
        if(len(val)==2):
            continue
        else:
            # print(val)
            # print(val[2])
            if(toNode==val[2]):
                listthis.append(val[2])
                # print("------------------")
                # print("found")
                # print(fromNode,val[1])
                # print(listthis)
                # print("------------------")
                return getMinDistance(fromNode,val[1],listthis,pathDict)



class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_edge('A','B',2)
g.add_edge('A','D',1)
g.add_edge('A','C',5)

g.add_edge('B','C',3)
g.add_edge('B','D',2)

g.add_edge('C','D',3)
g.add_edge('C','E',1)
g.add_edge('C','F',5)

g.add_edge('D','E',1)

g.add_edge('E','F',2)

def getResult(queryA,queryB):
    pathDict = {}

    for v in g:
        if(v.get_id()==queryA):  #change A to start
            pathDict[v.get_id()]=0,[]
        else:
            pathDict[v.get_id()]=math.inf,[]
        # for w in v.get_connections():
        #     vid = v.get_id()
        #     wid = w.get_id()
        #     print( vid, wid, v.get_weight(w))
    # print(pathDict)

    for v in g:
        
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            if(wid==queryA): #change to start
                continue
            else:
                strToStore = vid + "->"+ wid
                # print(strToStore, v.get_weight(w))
                cost = v.get_weight(w)
                if(pathDict[wid][0] > pathDict[vid][0] + cost):
                    # print("UPDATING BEFORE:")
                    # print(pathDict[wid])
                    pathDict[wid] = pathDict[vid][0] + cost,vid,wid
                    # print("UPDATING AFTER:")
                    # print(pathDict[wid])
            # print("=====================")

                # print(cost)

    # print(pathDict)
    answer = getMinDistance(queryA,queryB,[],pathDict)
    return answer


# print("ANSWER:",getResult('A','C'))




# APIs start
from flask import Flask

app = Flask(__name__)

@app.route('/getMinDistance', methods=['GET'])
def getMinDistanceAPP():
    fromQuery = request.args.get('fromQuery')
    toQuery = request.args.get('toQuery')
    result = getResult(fromQuery,toQuery)
    return '['+','.join(map(str, result)) + ']'


app.run()

print("running on http://127.0.0.1:5000/")



















    



