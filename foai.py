'''DEPTH FIRST SEARCH
  - USES STACK AND RECURSION
'''
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
        if visited[neighbour]==False:
            dfs(graph,neighbour,visited,path)
    return path

graph=defaultdict(list)
G=nx.Graph()

nodes,edges=map(int,input().split())
for _ in range(edges):
    u,v=map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)
    G.add_edge(u,v)

start=input()
visited=defaultdict(bool)
path=[]
traversedpath=dfs(graph,start,visited,path)
print(traversedpath)

fig, ax = plt.subplots(figsize=(6,6))  

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    ax=ax,               
    with_labels=True,
    node_color="lightblue",
    edge_color="red",
    node_size=2000,
    font_weight="bold"
)

plt.show()