'''
this is the community detection algorithm
author:JingChen
email:jingchen23@tongji.edu.cn
copyright 2016
'''

from igraph import *
import time
import math

class ODDWG:                #overlapped communities detection of weighted graph
    
    communities = []
    g = Graph()

    def __init__(self):
        print("init")
    
    def readGraph(self):
        self.g = load("F:\onedrive\project1\RandomGraph.gml",format="gml")
        return self.g

    def jaccard(self, community1, community2):
        coupling = len(list(set(community1).intersection(community2)))/len(list(set(community1).union(community2)))
        return coupling

    def mergeCommunity(self):              #jaccard method
        flag = 0
        while (flag == 0):
            flag = 1
            communities_num = len(self.communities)      #get the number of communities
            for i in range(communities_num-1):
                for j in range(i+1,communities_num): 
                    if(self.jaccard (self.communities[i], self.communities[j]) > 0.25):
                        self.communities.append(list(set(self.communities[i]).union(self.communities[j])))
                        self.communities.remove(self.communities[j])    #delete the larger index in case of the out-of-range problem
                        self.communities.remove(self.communities[i])                        
                        communities_num -= 1
                        flag = 0
                        break
                if (flag == 0):
                    break
        i = len(self.communities) - 1
        while(i > -1):
            if (len(self.communities[i]) <3):
                self.communities.remove(self.communities[i])
            i -= 1

        
    def addThe2V(self,edge,g):         #add the two endpoints into the community
        community = [edge.source,edge.target]
        for vertice in self.findTheNeighbors(edge,g):     #get the end points
            community.append(vertice)                     #get the neighbors
        self.communities.append(community)
        

    def findTheNeighbors(self,edge,g):   #find the common neighbors of the teo endpoints
        index1 = edge.source
        index2 = edge.target
        neighborhood1 = []
        neighborhood2 = []
        vs = VertexSeq(g)
        
        for v in vs[index1].neighbors():
            neighborhood1.append(int(v["id"]))
        for v in vs[index2].neighbors():
            neighborhood2.append(int(v["id"]))
        return list(set(neighborhood1).intersection(neighborhood2))
            

    def findNeighborhoods(self):   #find the neighborhoods
        g_temp = self.g.copy()
        edges = g_temp.es
        while (edges):
            temp_edge = edges[0]
            for edge in edges:
                if (temp_edge["Trust"] < edge["Trust"]):
                    temp_edge = edge
                self.addThe2V(temp_edge,self.g)
            edges.select(temp_edge.index).delete()  #delete the largest one

    '''
    def deleteOneWayEdge(self,es):
        board = es.is_mutual()
        i = len(board) - 1
        while (i > -1):                       #iterate from large to small to avoid the change problem
            if not (board[i]):
                es.select(i).delete()                   #delete the edge without a counterpart
            i -= 1
            
        print ("after deleteOneWayEdge:",int(len(es)/2),"pairs of mutual edges are left")
        return es
    '''
    def buildCommunity(self,g):
#        es = EdgeSeq(g)               get the edge sequence of the graph
#        print ("number of vertex:",len(g.vs))
#        print ("number of edges:",len(g.es))

        g.to_undirected(mode = "mutual", combine_edges = "product")
#       we can delete some too-low-trust edges here
        #es = self.deleteOneWayEdge(es)
#       self.g1 = g.copy()            #copy the graph at this point for the path finder

        self.findNeighborhoods()
        print ("findNeighborhoods done in", time.time() - t)
        '''
        while (g.es):                   #analyze the edges until it's empty
#           print ("edge:",edge.index)
           self.popLargestWE(es,g)    #the edgeseq without the edge with the largest weight
#            print (self.communities)
        '''
        self.mergeCommunity()

    def findShortestPath(self,g):     #find the shortest path between each two unlinked vertex in each community
        for edge in g.es:
            print(edge["Trust"])
            edge["Trust"] = - math.log(float(edge["Trust"]), 2)
    #        print(edge["Trust"])
        summary(g)
        for community in self.communities:
            matrix = g.shortest_paths_dijkstra(community,community,weights = 'Trust')
            print (matrix)

            i = 0
            while (i < len(matrix) - 1):
                j = i + 1
                while (j < len(matrix)):
                    if not(g.are_connected(community[i],community[j])):
                        g.add_edge(community[i],community[j])
                    g.es[g.get_eid(community[i],community[j])]['Trust'] = matrix[i][j]
                    j += 1
                i += 1
        showTheGraph(g)
        for edge in g.es:
            edge["Trust"] =  pow(2,-edge["Trust"])
            print(edge["Trust"])
        print ("compute the shortest paths done in", time.time()-t)
        summary(g)



#    def __del__(self):
#        print ("object gone")

x = ODDWG()
g = x.readGraph()   #read the graph from local directory
#print ("The ration of mutual ",g.reciprocity (ignore_loops = True, mode = "ratio"))

'''
def showTheGraph(g):
    g.vs["label"] = g.vs["id"]
    layout = g.layout("kk")
    plot(g, layout = layout, bbox = (300,300) , margin = 20)
'''

t = time.time()
x.buildCommunity(x.g)
x.findShortestPath(x.g)
print ("build communities done in", time.time() - t)

print("the communities are as follows:")
for i in x.communities:
    print(i)
print("we got", len(x.communities), "communities")
