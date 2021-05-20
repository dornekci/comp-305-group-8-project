import Node as n
import Edge as e
import Graph as g
import numpy as np
import time


def read_txt(path):

    # For checking the runtime of the program
    start_time = time.time()

    # Opening the file and writing the content to lines array
    with open(path) as f:
        lines = f.readlines()

    # Removing \n's from the lines
    new_lines = []
    for line in lines:
        line = line.replace('\n', '')
        new_lines.append(line)

    lines = new_lines

    graph = g.Graph()

    # Getting the vertex count from the data
    line = lines[0]
    N = int(line)
    lines.remove(line)
    graph.N = N

    # Getting the edge count from the data
    line = lines[0]
    E = int(line)
    lines.remove(line)
    graph.E = E

    # Getting the kingdom size from the data
    line = lines[0]
    M = int(line)
    lines.remove(line)
    graph.M = M

    node_lines = lines[:N]
    edge_lines = lines[N:]

    max_kingdom = 0
    i = 0
    for line in node_lines:

        info = line.split()
        id = int(info[0])
        kingdom = int(info[1])

        node = n.Node(id, kingdom, [], False)

        graph.nodes.append(node)
        print("Node added :", i)
        i += 1
        if kingdom > max_kingdom:
            max_kingdom = kingdom

    graph.K = max_kingdom

    j = 0
    for line in edge_lines:
        info = line.split()
        src = int(info[0])
        dst = int(info[1])

        edge = e.Edge(src, dst)
        graph.edges.append(edge)
        print("Edge added :", j)

        j += 1

    graph.neighbors_from_edges()


    print("Input reading finished in %.8s seconds" % (time.time() - start_time))

    return graph

if __name__ == '__main__':

    path = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test2_new.txt"

    graph = read_txt(path)
    graph.info()

    testGraph = g.Graph()

    node0 = n.Node(0, 0, [0, 1, 1, 0], False)
    testGraph.add_node(node0)

    node1 = n.Node(1, 1, [1, 0, 0, 0], False)
    testGraph.add_node(node1)

    node2 = n.Node(2, 2, [1, 0, 0, 1], False)
    testGraph.add_node(node0)

    node3 = n.Node(3, 0, [0, 1, 1, 0], False)
    testGraph.add_node(node3)

    node4 = n.Node(4, 1, [1, 1, 0, 0], False)
    testGraph.add_node(node4)

    edge01 = e.Edge(0, 1)
    testGraph.add_edge(edge01)

    edge02 = e.Edge(0, 2)
    testGraph.add_edge(edge02)

    edge05 = e.Edge(0, 5)
    testGraph.add_edge(edge05)

    edge27 = e.Edge(2, 7)
    testGraph.add_edge(edge27)



