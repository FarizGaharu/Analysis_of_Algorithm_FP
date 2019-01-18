'''
Analysis of Algorithm Final Project created by:
- Fariz Ihsan Yazid (2101677091)
- Alfi Redzwan (2101693574)
- Jason Erniody (2101693510)
'''

import prim_krus
city = open("KotaDataSet.csv", 'r') # dataset that we used for this project

graph = prim_krus.Graph() # for intializing the graph

for stream in city:                     # used for read the data sets that have been stored in city(variable)
    line = stream.split(',')
    graph.add_edge(line[0], line[1], int(line[2].strip('\n')))
    graph.add_node(line[0])

def main_menu():
    print(30 * "-", "Menu", 30 * "-")
    print("a. Undirected Graph")
    print("b. Prims")
    print("c. Kruskal")
    print("d. Exit")
    print(67 * "-")

    ulang = True

    while ulang:
        pilihan = input("Enter Your Choice:\n")

        if pilihan == "a": # this function is showing the undirected graph
            prim_krus.showgraph(graph)

        elif pilihan == "b": # this function is showing the directed graph using prims algorithms
            prim = prim_krus.prims(graph)
            prim_krus.showgraph(prim)

        elif pilihan == "c": # this function is showing the directed graph using kruskal algorithms
            krus = prim_krus.kruskal(graph)
            prim_krus.showgraph(krus)

        elif pilihan == "d": # exit function
            print("bye-bye")
            ulang = False

        else:
            exit()

main_menu()





