import Node as n
import Edge as e
import Graph as g
import numpy as np
import time

def read_txt(path):

    testGraph = g.Graph()

    node0 = n.Node(0, 0, [0, 1, 1, 0], False)
    testGraph.add_node(node0)

    node1 = n.Node(1, 1, [1, 0, 0, 0], False)
    testGraph.add_node(node1)

    node2 = n.Node(2, 2, [1, 0, 0, 1], False)
    testGraph.add_node(node0)

    node3 = n.Node(3, 0, [0, 1, 1, 0], False)
    testGraph.add_node(node3)

    node4 = n.Node(4, 1, [1,1,0,0], False)
    testGraph.add_node(node4)

    edge01 = e.Edge(0,1)
    testGraph.add_edge(edge01)

    edge02 = e.Edge(0,2)
    testGraph.add_edge(edge02)

    edge05 = e.Edge(0,5)
    testGraph.add_edge(edge05)

    edge27 = e.Edge(2,7)
    testGraph.add_edge(edge27)
    return 0

if __name__ == '__main__':

    # For checking the runtime of the program
    start_time = time.time()

    path = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test3_new.txt"

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

    max_kingdom = 0
    for i in range(N):

        line = lines[0]

        info = line.split()

        node = n.Node(int(info[0]), int(info[1]), [], False)

        graph.add_node(node)
        print("Node added :", i)
        lines.remove(line)

        if int(info[1]) > max_kingdom:
            max_kingdom = int(info[1])

    graph.K = max_kingdom

    j = 0
    for line in lines:

        info = line.split()

        edge = e.Edge(int(info[0]), int(info[1]))
        graph.add_edge(edge)
        print("Edge added :", j)

        graph.add_neighbor(int(info[0]), int(info[1]))
        graph.add_neighbor(int(info[1]), int(info[0]))
        j += 1

    graph.write_nodes()

    graph.sort_nodes()
    graph.write_nodes()
    graph.info()

    print("Finished in %.6s seconds" % (time.time() - start_time))





