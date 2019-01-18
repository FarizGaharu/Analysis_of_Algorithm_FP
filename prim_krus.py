'''
Analysis of Algorithm Final Project created by:
- Fariz Ihsan Yazid (2101677091)
- Alfi Redzwan (2101693574)
- Jason Erniody (2101693510)
'''

import networkx as nx                   # this two library used for plotting in the
import matplotlib.pyplot as plt

class Graph:
    def __init__(self): # initializing graph class
        self.nodes = set()
        self.edges = {}

    def add_node(self,val): # adding nodes
        self.nodes.add(val)

    def add_edge(self, from_node, to_node, distances): # adding edges
        self.edges[(from_node, to_node)] = distances

    def getNodes(self):  # return the nodes that already stored in graph
        return set(self.nodes)

    def getEdges(self):  # retun the edges that already stored in graph
        return dict(self.edges)

    def getWeight(self, undirected=True): # return the edges that already stored in graph
        if undirected:
            return sum(self.edges.values()) / 2

class PStack: # Tailor made for storing edges
    def __init__(self):
        self.stack = []

    def append(self, val):
        self.stack.append(val)

    def pop(self):
        lowest_val = min(self.stack, key=lambda x: x[1])
        index_lowest_val = self.stack.index(lowest_val)
        return self.stack.pop(index_lowest_val)

    def isEmpty(self):
        return not bool(self.stack)


def showgraph(graph): # use for showing graph of the dataset
    gr_edge = []
    gr_label = {}
    for key, value in graph.edges.items():
        gr_edge.append(key)
        gr_label[key] = value

    GR = nx.Graph()
    GR.add_edges_from(gr_edge)
    position = nx.kamada_kawai_layout(GR)
    nx.draw(GR,position, font_size=10, node_color='lime', node_size=100, with_labels=True)
    nx.draw_networkx_edge_labels(GR, position, font_size=10, font_color='blue',edge_labels=gr_label,rotate=0)

    plt.show()

def prims(graph):
    result_gr = Graph()
    nodes = graph.getNodes()
    edges = graph.getEdges()

    p_edgy = PStack() # populated once touched by a current_node

    start = sorted(list(nodes))[0]

    result_gr.nodes = nodes
    lewat =[start]
    curr_node = start

    while(sorted(lewat) != sorted(nodes)):
        for edge in edges.keys(): # Iterates through all the edges (src, dst)
            if edge[0] == curr_node and not edge[1] in lewat:
                p_edgy.append((edge, graph.edges[edge]))

        while curr_node in lewat:
            curr_edge = p_edgy.pop()
            curr_node = curr_edge[0][1] # sets the destination node (dst) from ((src, dst), weight) as the the next node that will be worked on

        result_gr.add_edge(curr_edge[0][0], curr_edge[0][1], curr_edge[1])
        result_gr.add_edge(curr_edge[0][1], curr_edge[0][0], curr_edge[1])

        lewat.append(curr_node) # Marks the current node as visited
    return result_gr


def kruskal(graph):
    nodes = graph.getNodes()
    edges = graph.getEdges()
    result_gr = Graph()
    pairs = PStack()

    for node, weight in edges.items():
        pairs.append((node, weight))

    disj_set = [[x] for x in nodes] # disj is equal to disjoint
    loc_set = {nodes.pop(): x for x in range(len(nodes))} #loc_is equal to location

    while len(disj_set) > 1:
        curr_pair = pairs.pop()

        if not (curr_pair[0][0] in disj_set[loc_set[curr_pair[0][1]]]):
            result_gr.add_edge(curr_pair[0][0], curr_pair[0][1], curr_pair[1])
            result_gr.add_edge(curr_pair[0][1], curr_pair[0][0], curr_pair[1])

            disj_set[loc_set[curr_pair[0][0]]] = disj_set[loc_set[curr_pair[0][0]]] + disj_set[loc_set[curr_pair[0][1]]]
            disj_set.pop(loc_set[curr_pair[0][1]])

            for location in range(loc_set[curr_pair[0][1]], len(disj_set)):
                for x in disj_set[location]:
                    loc_set[x] = loc_set[x] - 1

            for location in disj_set[loc_set[curr_pair[0][0]]]:
                loc_set[location] = loc_set[curr_pair[0][0]]

    return result_gr









