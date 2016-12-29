from igraph import *
#下面的代码是用来生成随机图的
import random
import math

vertexNum = 10
edgeNum = 40

g = Graph.Erdos_Renyi(n = vertexNum,m = edgeNum,directed = True)
for i in range(edgeNum):
    root = random.uniform(0.1,1)
    g.es[i]["Trust"] = root
'''
for i in range(edgeNum):
    root = random.uniform(1,100)
    g.es[i]["Trust"] = round(root*root/10000, 3)
'''
'''
for i in range(1000):
    addDish = random.uniform(1,10000)
    addDrink = random.uniform(1,10000)
    if g.
'''
summary(g)
print(g)
'''
visual_style = {}
visual_style["vertex_label"] = g.vs["num"]
visual_style["vertex_size"] = 20
visual_style["layout"] = layout
visual_style["bbox"] = (300, 300)
visual_style["margin"] = 20
#visual_style["edge_lenth"] = g.es["Trust"]

#g.vs["label"] = g.vs[""]
layout = g.layout("kk")
plot(g, layout = layout, bbox = (300,300) , margin = 20)

communities = g.community_leading_eigenvector(weights = g.es["Trust"])
print (communities)
#covers = communities.as_cover()
#clusters = communities.as_clustering()  #n表示分成几个cluster
'''
g.save("F:\onedrive\project1\RandomGraph.gml",format="gml")
'''

#从本地读取图
g = load("F:\onedrive\project1\RandomGraph.gml",format="gml")
summary(g)
#对图进行聚类
下面的代码是用来看是否是我想要的幂律分布的

count = []
for i in range(100):
    count.append(0)
for i in range(20):
    count[g.es[i]["Trust"]] += 1

for i in count:
    i /= 20

print (count)
'''

    

